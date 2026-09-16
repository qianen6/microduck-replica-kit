# Chinese actuator candidates

There is no zero-change domestic drop-in for the XL330 baseline. The useful distinction is between a **same-size experimental candidate** and a **larger, mature redesign route**.

| Candidate | Public specification | Fit verdict |
|---|---|---|
| DSpower DS-S009C TTL | 23×12×26.5 mm; vendor claims 9 g; 6–7.4 V; magnetic encoder; TTL; up to 11 kgf·cm static stall | highest-priority one-unit bench candidate; mounting, protocol revision and sustained torque require measurement |
| Feetech STS3032 / STS3036 | 17.7–20.6 g; about 4.5 kgf·cm at 6 V; TTL bus; 12-bit feedback | suitable for head/beak experiments or a lighter/slower retrained design |
| Unitree S288 | 20×34×26 mm; 19.5 g; 288.35:1; 12.6 V; 6 Mbps; dual encoder | near-perfect envelope but published torque is below the leg target |
| Unitree J288 | same envelope; 35 g; up to 1.5 N·m; 25.2 V | torque-capable but changes mass, voltage and control stack |
| Feetech STS3215 | 55 g; ~19.5 kgf·cm at 7.4 V | mature low-cost route for a larger ~42 cm Open Duck Mini-style robot |

## DS-S009C sample gate

Before a 15-unit decision, measure one current-revision TTL sample:

- actual mass and dimensions;
- continuous 0.45 N·m load for 10 minutes;
- backlash and return error;
- no-load speed;
- supported baud rates, ID range and broadcast write;
- complete 15-device command + state cycle under 20 ms;
- current and temperature under repeated impact-like trajectories.

The public model name has appeared with different historic torque/protocol descriptions. Record the PCB/firmware revision and archive the exact datasheet received with the sample.

## Software impact

Replacing XL330 changes the packet protocol, mounting zero, actuator response, friction/backlash and supply-current model. A serious replacement therefore includes:

1. a new bus driver;
2. actuator identification;
3. updated MuJoCo/BAM parameters;
4. domain randomization around measured variance;
5. policy retraining and suspended-robot validation.

