# WORK IN PROGRESS
# 3D Printed Chess
This repository contains the info and software to build a home made electronic chessboard.

**Features**
- Pieces movements are detected automatically
- Computer movements are showed using the leds
- [Stockfish](https://stockfishchess.org/) used as chess engine

## General design
The board is designed to be 3D printed. The pieces are also 3D printed and each one has a magnet atached on the bottom. Each cell of the board has a magnetic sensor and a RGB led. The sensors and the leds are controled by the Arduino Nano. The Arduino Nano is connected using the USB cable to the Raspberry Pi and they comunicate using Serial messages. The Raspberry Pi is running the main program.

## 3D printing
The board and the pieces have been printed using a 3D printer in white and black PLA.

### Board

### Pieces


## Software



## Material list
This is the main material used to make this project. You should be able to replace the components for similar ones. For example, a Raspberry Pi 1/2 should work but it has not been tested. You should be able to buy the components where you want. The buy link is the site were I purchased the components.

- **64 x WS2812B LEDs**. Estimated price 8€/100 units. [Buy](https://aliexpress.com/item/5-1000pcs-LED-Board-Heatsink-ws2812b-LED-chips-With-Black-White-PCB-10mm-3mm-WS2811-IC/32833250841.html)
- **64 x SS49E**. Estimated price 8€/100 units. [Buy](https://aliexpress.com/item/100PCS-Hall-Element-49E-OH49E-SS49E-linear-Hall-Switch/32416157741.html)
- **4 x CD74HC4067** Estimated price 6.5€/4 unit. [Buy](https://aliexpress.com/item/1pcs-CD74HC4067-16-Channel-Analog-Digital-Multiplexer-Breakout-Board-Module-For-Arduino/32729631800.html)
- **32 x Neodimiun magnets** Estimated price 3.70€/50 units. [Buy](https://aliexpress.com/item/50pcs-12x2mm-Super-Strong-magnet-Round-Disc-Rare-Earth-Neodymium-magnets-D12-2mm-NEW-Art-Craft/32851739554.html)
- **1 x Arduino nano + Usb cable**. Estimated price 3€
- **1 x Raspberry Pi 3+** Estimated price 35€
- **1 x Raspberry Pi power adapter** Estimated price 12€
- **1 x Micro SD card** Estimated price 10€
- **1 x 5 volt 2 amp power supply for the leds** Estimated price 12€
- **3 x buttons or 1 x rotary encoder with push button** 

**Total estimated price: 97.60€**
The estimated price can be lowered if you already have some of the materials already. For example, It is usual to have a Micro SD card and phone charges that can be used to power the leds and the Raspberry Pi, lowering the price to **63.60€**.

# Power supply
The Raspberry Pi should be powered using a good 5v power adapter with enough amperage. You can use the official one to avoid problems. The arduino nano is connected to the Raspberry Pi Usb port and it will get the power directly from the Raspberry Pi.

The biggest power draw comes from the WS2812B leds. Each led can draw up to 60mA in the max brigthness. So theorically the leds could draw up to 64x60mA=3840mA. The reallity is that the duty cycle is limited to half from code with little impact for the percieved brigthness ([More info](https://learn.adafruit.com/sipping-power-with-neopixels?view=all#strategy-gamma-correction)), so the max draw should not be higger than 64x30mA=**1920mA**. This is the worst case scenario (all the leds showing white), in general the consumption will be lowerr as some leds will be off or showing another color that draws less. Because of this, a power supply of 2 amps should be enough even for the worst case.


