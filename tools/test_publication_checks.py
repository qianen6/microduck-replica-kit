"""Regression checks for privacy detection without storing live credentials."""
from verify_publication import check_text
import unittest

class PrivacyChecks(unittest.TestCase):
    def rejected(self,value):
        with self.assertRaises(AssertionError):check_text(value,'synthetic')
    def test_token(self):self.rejected('ghp_'+'x'*30)
    def test_email(self):self.rejected('private'+'@'+'example.net')
    def test_home(self):self.rejected('C:'+chr(92)+'Users'+chr(92)+'private'+chr(92)+'data')
    def test_file_browser_padding(self):self.rejected('Users'+chr(92)+'private'+chr(92)+'OneDrive')
    def test_network(self):self.rejected('.'.join(['192','168','10','42']))
    def test_wechat(self):self.rejected('wxid_'+'syntheticuser')
    def test_upstream_url(self):check_text('https://github.com/pollen-robotics/microduck','public')
    def test_dimensions(self):check_text('25 x 24 mm; 21 x 12.5 mm; 6.4 V','engineering')

if __name__=='__main__':unittest.main()
