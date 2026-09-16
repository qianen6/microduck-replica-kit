# Functional-compatible Rev A

## Target

`functional_compatible_rev_a` preserves the public kinematic layout and the upstream 61-observation / 14-policy-action contract while replacing unavailable manufacturing data with staged measurement and self-designed electronics.

## Architecture

| Subsystem | Rev A target | Evidence state |
|---|---|---|
| Compute | Radxa Zero 3W, RK3566 | high confidence from runtime/device-tree evidence |
| Actuation | 15 compact smart servos; XL330-compatible baseline | high confidence for count and bus layout |
| Policy joints | 14; mouth excluded from policy action | verified in runtime/model |
| Servo bus | UART2, 1 Mbps, 3.3 V TTL half duplex | verified in runtime |
| IMU | LSM6DSV16X, Dynamixel-like ID 200 prototype | data contract verified; PCB absent |
| Depth | VL53L8CX-class 8×8 ToF | optional until locomotion bring-up |
| Camera | IMX219-class CSI camera | optional until locomotion bring-up |
| Battery | removable pack; final rail frozen after bench test | hardware implementation unresolved |
| Audio/NFC | deferred from locomotion Rev A | not required by 50 Hz control loop |

## Stage gates

| Gate | Build | Pass condition |
|---|---|---|
| G0 | source-only | locked commits and deterministic reference export |
| G1 | one actuator | 50 Hz for 30 min; current, voltage, temperature and packet-loss log |
| G2 | print coupon | repeatable M2 insert and bearing fits |
| G3 | one leg | full travel, no harness pinch, 10 min static support |
| G4 | full bus | 15 actuators + IMU; complete read/write within 20 ms |
| G5 | suspended robot | home, sit/stand and fall-to-limp before gait execution |

## Key design rule

Do not bulk-purchase the remaining actuators or freeze battery/PCB design before G1 and G2. The first prototype is a measurement instrument, not a production unit.

