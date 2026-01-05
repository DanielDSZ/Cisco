# RGB LED Crossfade (Smooth Color Transitions) — Cisco Packet Tracer

## Overview
This project demonstrates **PWM-based RGB color blending** in **Cisco Packet Tracer (IoT)** using a **Microcontroller Unit (MCU)** and an **RGB LED**. Instead of switching channels on/off, the program uses `analogWrite` to smoothly **crossfade** between colors by increasing one channel while decreasing another.

The result is a continuous, professional-looking transition:
- **Red → Green**
- **Green → Blue**
- **Blue → Red**
…and repeats forever.

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## Features
- Smooth RGB crossfading using PWM (`analogWrite`)
- No abrupt color changes (blended transitions)
- Adjustable smoothness (step size) and speed (delay)
- Clean initialization (all channels OFF before each cycle)

## Requirements
- Cisco Packet Tracer (IoT-enabled version)
- IoT MCU device
- RGB LED device
- IoT Custom Cable (for wiring)

## Hardware / Topology
- **MCU Output Slots:** `0`, `1`, `2` (configured as `OUTPUT`)
- **RGB Channels:**
  - Slot `0` → Red
  - Slot `1` → Green
  - Slot `2` → Blue
- **PWM Range:** `0` to `1023` (typical Packet Tracer IoT scale)

> **Note:** Some RGB modules behave differently depending on common anode/cathode wiring. If colors look inverted, you may need to swap `0` and `1023` for the affected channels.

## Wiring
1. Place an **MCU** and an **RGB LED** in the workspace.
2. Select **IoT Custom Cable**.
3. Connect:
   - **MCU slot 0** → **RGB Red**
   - **MCU slot 1** → **RGB Green**
   - **MCU slot 2** → **RGB Blue**

## Program Logic (Blockly)
### 1) Pin Configuration
The program sets all three channels as outputs:
- `pinMode(slot 0, OUTPUT)`
- `pinMode(slot 1, OUTPUT)`
- `pinMode(slot 2, OUTPUT)`

### 2) Main Loop (Crossfade Sequence)
Inside an infinite loop:
1. **Reset all channels to OFF**
   - `analogWrite(0, 0)`
   - `analogWrite(1, 0)`
   - `analogWrite(2, 0)`
   - `delay(200 ms)`

2. **Crossfade Red → Green**
   - Red decreases: `1023 - i`
   - Green increases: `i`
   - Blue stays OFF: `0`

3. **Crossfade Green → Blue**
   - Green decreases: `1023 - i`
   - Blue increases: `i`
   - Red stays OFF: `0`

4. **Crossfade Blue → Red**
   - Blue decreases: `1023 - i`
   - Red increases: `i`
   - Green stays OFF: `0`

Each crossfade uses:
- `count with i from 0 to 1023 by 25`
- `delay(10 ms)` between steps

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## How to Run
1. Open the `.pkt` file in Cisco Packet Tracer.
2. Open the MCU → **Programming** tab → **Blockly**.
3. Load or recreate the blocks, then click **Run**.
4. Observe smooth color transitions across the RGB LED.

## Tuning (Make It Smoother or Faster)
- **Step size (`25`)**
  - Smaller (e.g., `10`) = smoother transitions
  - Larger (e.g., `50`) = faster but more “stepped”
- **Delay (`10 ms`)**
  - Lower = faster crossfade
  - Higher = slower crossfade
- **Inter-cycle delay (`200 ms`)**
  - Increase for a noticeable pause between full transitions

## Troubleshooting
- **LED stays off**
  - Confirm wiring and correct slot-to-channel mapping (0=R, 1=G, 2=B).
  - Ensure the MCU pins are set to `OUTPUT`.
- **Colors look inverted**
  - Try inverting PWM values for a channel: use `(1023 - value)` vs `value`.
- **Transitions look choppy**
  - Reduce step size (e.g., `25` → `10`) and/or increase delay slightly.

## Improvements / Next Steps
- Add a **button** to switch between patterns (Sequence / Crossfade / Blink / Off)
- Add a **potentiometer or LDR** to control transition speed dynamically
- Implement full-spectrum color wheel blending (HSV-like behavior with RGB output)
- Add debug output (log current `i` and channel values)

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Deploy

Para fazer o deploy desse projeto rode

```bash
  npm run deploy
```


## Licença

[MIT](https://choosealicense.com/licenses/mit/)

