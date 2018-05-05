# WORK IN PROGRESS
# 3D Printed Chess
This repository contains the info and software to build a home made electronic chessboard.

**Features**
- Pieces movements are detected automatically
- Computer movements are showed using the leds
- [Stockfish](https://stockfishchess.org/) used as chess engine

## General design
The board is designed to be 3D printed. The pieces are also 3D printed and each one has a magnet atached on the bottom. Each cell of the board has a magnetic sensor and a RGB led. The sensors and the leds are controled by the Arduino Nano. The Arduino Nano is connected using the USB cable to the Raspberry Pi and they comunicate using Serial messages. The Raspberry Pi is running the main program.

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

**Total estimated price: 97.60€**
The estimated price can be lowered if you already have some of the materials already. For example, It is usual to have a Micro SD card and phone charges that can be used to power the leds and the Raspberry Pi, lowering the price to **63.60€**.

# Power supply
The Raspberry Pi


