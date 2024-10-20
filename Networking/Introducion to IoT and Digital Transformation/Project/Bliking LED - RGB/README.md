## LED Blinking with MCU

This flowchart represents a program designed to make an LED blink using a **Microcontroller Unit (MCU)** in **Cisco Packet Tracer**.

1. **Pin Mode Setup**: 
   - The **pinMode** block configures **slot 1** of the MCU as an **OUTPUT**, allowing it to send signals to the connected LED.

2. **Loop (Repeat While True)**:
   - The program enters an infinite loop (`while true`), repeatedly executing the steps to control the LED brightness.

3. **Analog Write**:
   - **analogWrite** sends different values (intensity levels) to **slot 1**. These values correspond to the brightness levels of the LED. The values range from **100** (low brightness) to **1023** (maximum brightness).
   - After each `analogWrite`, the program pauses for **500 ms** using the **delay** block.

4. **Brightness Control**:
   - The LED brightness gradually increases in steps: 
     - First, it is set to **100**.
     - Then to **500**, followed by **700**, and finally **1023** for full brightness.
   
This setup creates a **pulsing effect**, where the LED gradually brightens and remains in a loop, continuously repeating this sequence.


### Screenshots

![LED]([https://via.placeholder.com/468x300?text=App+Screenshot+Here](https://github.com/DanielDSZ/Cisco/blob/main/Networking/Introducion%20to%20IoT%20and%20Digital%20Transformation/Project/Bliking%20LED%20-%20RGB/LED.png))

## RGB LED Control with MCU

This flowchart demonstrates a program that controls an **RGB LED** using a **Microcontroller Unit (MCU)** in **Cisco Packet Tracer**. The RGB LED is connected to three different pins, each controlling one color channel (Red, Green, and Blue).

1. **Pin Mode Setup**: 
   - The **pinMode** blocks set **slots 0, 1, and 2** as **OUTPUT**. These correspond to the Red, Green, and Blue channels of the RGB LED.

2. **Loop (Repeat While True)**:
   - The program enters an infinite loop (`while true`), cycling through various color combinations by adjusting the values of each channel.

3. **Digital Write and Timing**:
   - The **digitalWrite** function sends values (either **1023** for ON or **0** for OFF) to each slot. This controls the intensity of each color channel.
     - The Red channel (**slot 0**) is turned ON first for **1000 ms**.
     - Then, the Green channel (**slot 1**) is activated while turning off the Red channel.
     - Afterward, the Blue channel (**slot 2**) is turned ON while turning off the Green channel.
   - Each color change occurs with a **1000 ms** delay between transitions, allowing visible changes in the LED's color.

4. **RGB Transitions**:
   - The program cycles through different color states, one at a time, controlling the Red, Green, and Blue components of the RGB LED in sequence:
     1. Red ON, Green and Blue OFF.
     2. Green ON, Red and Blue OFF.
     3. Blue ON, Red and Green OFF.

This setup creates a **color-cycling effect**, where the RGB LED transitions between red, green, and blue, looping indefinitely.## RGB LED Control with MCU

This flowchart demonstrates a program that controls an **RGB LED** using a **Microcontroller Unit (MCU)** in **Cisco Packet Tracer**. The RGB LED is connected to three different pins, each controlling one color channel (Red, Green, and Blue).

1. **Pin Mode Setup**: 
   - The **pinMode** blocks set **slots 0, 1, and 2** as **OUTPUT**. These correspond to the Red, Green, and Blue channels of the RGB LED.

2. **Loop (Repeat While True)**:
   - The program enters an infinite loop (`while true`), cycling through various color combinations by adjusting the values of each channel.

3. **Digital Write and Timing**:
   - The **digitalWrite** function sends values (either **1023** for ON or **0** for OFF) to each slot. This controls the intensity of each color channel.
     - The Red channel (**slot 0**) is turned ON first for **1000 ms**.
     - Then, the Green channel (**slot 1**) is activated while turning off the Red channel.
     - Afterward, the Blue channel (**slot 2**) is turned ON while turning off the Green channel.
   - Each color change occurs with a **1000 ms** delay between transitions, allowing visible changes in the LED's color.

4. **RGB Transitions**:
   - The program cycles through different color states, one at a time, controlling the Red, Green, and Blue components of the RGB LED in sequence:
     1. Red ON, Green and Blue OFF.
     2. Green ON, Red and Blue OFF.
     3. Blue ON, Red and Green OFF.

This setup creates a **color-cycling effect**, where the RGB LED transitions between red, green, and blue, looping indefinitely.
### Screenshots

![LED RGB]([https://via.placeholder.com/468x300?text=App+Screenshot+Here](https://github.com/DanielDSZ/Cisco/blob/main/Networking/Introducion%20to%20IoT%20and%20Digital%20Transformation/Project/Bliking%20LED%20-%20RGB/RGB.png))

