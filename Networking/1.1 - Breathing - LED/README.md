# MCU LED Fade (Breathing LED) — Cisco Packet Tracer

## Overview
This project demonstrates basic embedded-style I/O control in **Cisco Packet Tracer (IoT)** using a **Microcontroller Unit (MCU)** and a single **LED**. The LED brightness smoothly increases and decreases in a continuous loop using PWM-style output via `analogWrite`, creating a “breathing” (fade in/out) effect.

## Features
- Smooth LED brightness ramp-up and ramp-down (breathing effect)
- Adjustable fade speed and smoothness (step size and delay)
- Uses Packet Tracer IoT MCU Blockly program (visual programming)

## Requirements
- Cisco Packet Tracer (IoT-enabled version)
- IoT MCU device
- LED device
- IoT Custom Cable (for wiring)

## Hardware / Topology
- **MCU Output Slot:** `1` (configured as `OUTPUT`)
- **LED Input Pin:** connect to the corresponding LED pin (e.g., `D0`, depending on the LED module)
- **Cable:** IoT Custom Cable

> **Note:** In Cisco Packet Tracer IoT environments, PWM/analog output often uses a **0–1023** range (10-bit scale) for duty cycle/brightness values.

## Wiring
1. Place an **MCU** and an **LED** in the workspace.
2. Select **IoT Custom Cable**.
3. Connect:
   - **MCU D1** → **LED D0** (or the LED pin used in your topology)

![App Screenshot](https://github.com/DanielDSZ/Cisco/blob/main/Networking/1.1%20-%20Breathing%20-%20LED/docs/Breathing%20LED%201.png)

## Program Logic (Blockly)
1. Set the output slot as OUTPUT:
   - `pinMode(slot 1, OUTPUT)`
2. Run forever:
   - Count `i` from `0` to `1023` (step `+25`)
     - `analogWrite(slot 1, i)`
     - `delay(10 ms)`
   - Count `i` from `1023` to `0` (step `-25`)
     - `analogWrite(slot 1, i)`
     - `delay(10 ms)`
     
![App Screenshot](https://github.com/DanielDSZ/Cisco/blob/main/Networking/1.1%20-%20Breathing%20-%20LED/docs/Breathing%20LED%202.png)

### Suggested Parameters
- **Step size (`25`)**
  - Lower values = smoother fade (more steps)
  - Higher values = faster, more “stepped” fade
- **Delay (`10 ms`)**
  - Lower values = faster breathing
  - Higher values = slower breathing

## How to Run
1. Open the `.pkt` file in Cisco Packet Tracer.
2. Open the MCU → **Programming** tab → **Blockly**.
3. Load or paste the blocks, then click **Run**.
4. Observe the LED brightness smoothly fading in and out.

## Troubleshooting
- **LED does not light up**
  - Verify wiring (correct MCU pin to correct LED pin).
  - Confirm `pinMode(slot 1, OUTPUT)` is set.
  - Ensure the brightness value reaches a non-zero level (e.g., `1023`).
- **Fade only goes up but not down**
  - The decreasing loop must start at `1023` and count down to `0` using a negative step.

## Improvements / Next Steps
- Add a **button** to switch modes (OFF / BLINK / BREATHE)
- Add an **LDR (light sensor)** so ambient light controls brightness
- Add **serial/log output** for debugging (print brightness values)
- Extend to **RGB LED** with independent channel control and patterns

## License
[MIT](https://github.com/DanielDSZ/Cisco/blob/main/Networking/1.1%20-%20Breathing%20-%20LED/docs/LICENSE.txt)


