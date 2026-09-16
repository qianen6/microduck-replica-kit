# Rev A open gaps and closure tests

| ID | Gap | Evidence now | Measurement / prototype | Closed when |
|---|---|---|---|---|
| P0-MECH-01 | Simulation mesh lacks fit tolerances | 47 source STL + MJCF kinematic tree | Print M2 and bearing coupon at ±0.00/0.10/0.20/0.30 mm compensation | One compensation table produces repeatable press/slip fits |
| P0-ELEC-01 | `imu_to_dxl` schematic and firmware absent | ID 200; 1 Mbps V2; register 124; 12-byte block recovered from runtime | MCU + LSM6DSV16X prototype answers ping and sync-read alongside one servo | 30-minute 50 Hz read has no stale-run warning and orientation reaches ready |
| P0-PWR-01 | Inferred 2S rail conflicts with XL330 6.0 V rating | Runtime battery constants 6.6/8.2 V; vendor range 3.7–6.0 V | Single-servo stepped-supply characterization with current and temperature log | A documented rail voltage/current limit passes G1 and is reflected in simulation |
| P0-HARNESS-01 | Cable routing absent | Assembly geometry only | One-leg harness mock-up through full joint travel | No pinch/rub and service loop remains at every joint limit |

## Do not freeze before measurements

- Final battery topology and rail voltage.
- Production PCB outline, connectors and copper width.
- Global FDM hole compensation.
- Remaining fourteen actuator purchases.
- Use of the shipped ONNX policies without retraining.
