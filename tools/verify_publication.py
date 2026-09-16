#!/usr/bin/env python3
"""Dependency-free publication checks; no network or machine control."""
from pathlib import Path
import hashlib,json,re,struct,sys,zipfile
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'proof/release-manifest.json'
SKIP={'proof/release-manifest.json','VERIFICATION.txt'}
TEXT={'.md','.txt','.json','.csv','.py','.ps1','.sh','.yml','.yaml','.ino','.diff','.xml','.config','.model'}
PATTERNS={
 'credential':re.compile(r'(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9_-]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)'),
 'local_path':re.compile(r'(?i)(?<![a-z])(?:[a-z]:[/\\]+(?:Users|duck|ProgramData|Program Files)|[a-z]:[/\\][\w .-]+[/\\])|/(?:home|Users|mnt/data)/[\w.-]+|Users\\[^\\\x00]+\\OneDrive'),
 'account':re.compile(r'(?i)\bwxid_[a-z0-9_]+\b'),
 'private_ip':re.compile(r'(?<![\d.])(?:192\.168\.\d+\.\d+|10\.\d+\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)(?![\d.])'),
 'email':re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'),
}
def files():
 return sorted(p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check_text(text,label):
 for name,pat in PATTERNS.items():
  if pat.search(text):raise AssertionError('privacy '+name+' in '+label)
def local_links(text,p):
 refs=re.findall(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)',text)+re.findall(r'(?:src|href)="([^"]+)"',text)
 for ref in refs:
  if re.match(r'^[a-zA-Z]+:',ref) or ref.startswith('#'):continue
  q=(p.parent/unquote(ref.split('#')[0])).resolve()
  assert q.is_relative_to(ROOT) and q.exists(),'broken link '+str(p.relative_to(ROOT))+' -> '+ref
def png(data):
 assert data.startswith(b'\x89PNG\r\n\x1a\n');i=8
 while i<len(data):
  n=struct.unpack('>I',data[i:i+4])[0];kind=data[i+4:i+8]
  assert kind not in {b'tEXt',b'zTXt',b'iTXt',b'eXIf'},'PNG metadata'
  i+=n+12
def jpeg(data):
 assert data.startswith(b'\xff\xd8');i=2
 while i<len(data):
  assert data[i]==255;marker=data[i+1]
  if marker==0xda:return
  assert not (0xe1<=marker<=0xef or marker==0xfe),'JPEG metadata'
  i+=2+int.from_bytes(data[i+2:i+4],'big')
def validate():
 fs=files()
 for p in fs:
  rel=p.relative_to(ROOT).as_posix()
  assert p.stat().st_size<95*1024*1024,'oversize '+rel
  assert not any(x in {'.env','.venv','node_modules','apps','downloads','work'} for x in p.relative_to(ROOT).parts),'workspace leakage'
  assert p.suffix.lower() not in {'.log','.gcode','.zip','.xlsx','.pem','.key','.blend1'},'unreviewed file '+rel
  check_text(rel,rel)
  if p.suffix in TEXT or p.name in {'.gitignore','LICENSE'}:
   text=p.read_text(encoding='utf-8-sig');check_text(text,rel)
   if p.suffix=='.md':local_links(text,ROOT/'README.md' if rel=='proof/README.original.md' else p)
  elif p.suffix=='.blend':
   data=p.read_bytes();assert data.startswith(b'BLENDER')
   for match in re.finditer(rb'[ -~]{8,}',data):check_text(match[0].decode('ascii'),rel)
  elif p.suffix=='.stl':
   data=p.read_bytes();n=struct.unpack('<I',data[80:84])[0]
   assert len(data)==84+50*n and data[:80].startswith(b'Microduck R9 trial'),rel
  elif p.suffix=='.png':png(p.read_bytes())
  elif p.suffix=='.jpg':jpeg(p.read_bytes())
  elif p.suffix=='.3mf':
   with zipfile.ZipFile(p) as z:
    assert z.testzip() is None
    for name in z.namelist():
     assert not name.startswith('/') and '..' not in Path(name).parts
     data=z.read(name)
     if Path(name).suffix in TEXT:check_text(data.decode('utf-8'),rel+'!'+name)
    s=json.loads(z.read('Metadata/project_settings.config'))
    assert s['enable_support']=='1' and s['support_type']=='tree(auto)'
    assert len([n for n in z.namelist() if n.startswith('3D/Objects/')])==11
 for f in ['README.md','docs/images/wechat-group.jpg','models/r9/Microduck_R9_trial.blend','printing/r9/R9_11_parts_support.3mf','proof/blender-sanitization.json','proof/3mf-sanitization.json','ROLLBACK.sh','VERIFICATION.txt']:assert (ROOT/f).is_file(),f
 parts=json.loads((ROOT/'models/r9/parts-manifest.json').read_text())
 assert len(parts)==39 and len(list((ROOT/'models/r9/stl').glob('*.stl')))==39
 for row in parts:assert sha(ROOT/'models/r9'/row['file'])==row['sha256']
 assert 'release_snapshot: r9_2026_09_16' in (ROOT/'README.md').read_text(encoding='utf-8')
 report=json.loads((ROOT/'proof/blender-sanitization.json').read_text())
 assert report['geometry_transforms_material_assignments_unchanged'] and report['print_parts']==39 and not report['manufacturing_release']
 return fs
def main():
 mode=sys.argv[1]
 if mode in {'baseline','rollback'}:
  p=ROOT/'proof/README.original.md' if mode=='baseline' else Path(sys.argv[2]).resolve()
  assert sha(p)==sha(ROOT/'proof/README.original.md')
  assert 'repository_state: public_ready' in p.read_text(encoding='utf-8')
  assert 'release_snapshot: r9_2026_09_16' not in p.read_text(encoding='utf-8')
  print(mode.upper()+' PASS readme=PRE_R9 hash=MATCH');return
 fs=validate()
 actual={p.relative_to(ROOT).as_posix():sha(p) for p in fs if p.relative_to(ROOT).as_posix() not in SKIP}
 if mode=='manifest':
  MANIFEST.write_text(json.dumps(actual,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('MANIFEST PASS files='+str(len(actual)));return
 assert mode=='modified'
 assert actual==json.loads(MANIFEST.read_text(encoding='utf-8')),'release manifest mismatch'
 print('MODIFIED PASS stl=39 3mf_parts=11 support=1 privacy_findings=0 links=OK hashes=OK')
if __name__=='__main__':main()
