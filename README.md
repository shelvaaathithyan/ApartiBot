# ApartiBot

ApartiBot is a Raspberry Pi based keypad-controlled locker system with an LCD status display. It uses GPIO outputs to control four trays or box locks and opens each tray when the correct PIN is entered on a 4x4 keypad.

## Overview

The current implementation does the following:

- Shows a startup message on the LCD.
- Waits for keypad input.
- Accepts a 4-digit password.
- Unlocks one of four trays when the matching code is entered.
- Displays status messages such as successful access or wrong password.

This project is built around Raspberry Pi GPIO control and is intended for a physical hardware setup.

## Features

- 4x4 matrix keypad input
- LCD feedback for startup, entered keys, access granted, and errors
- Four independent tray/box outputs
- Raspberry Pi GPIO control using BCM numbering
- Simple password-based access logic

## Hardware Required

- Raspberry Pi
- 4x4 matrix keypad
- LCD display compatible with the `rpi_lcd` library
- Four relay modules, solenoids, or lock mechanisms
- Jumper wires and power supply suitable for the hardware

## Software Requirements

- Python 3
- `RPi.GPIO`
- `rpi_lcd`
- `pad4pi`

Install the Python dependencies with:

```bash
pip install RPi.GPIO rpi_lcd pad4pi
```

On some Raspberry Pi systems, you may need to use `pip3` instead of `pip`.

## GPIO Pin Mapping

The current script uses BCM numbering.

### Tray / Lock Outputs

- Tray 1: GPIO 17
- Tray 2: GPIO 18
- Tray 3: GPIO 15
- Tray 4: GPIO 14

### Keypad Pins

Rows:

- Row 1: GPIO 16
- Row 2: GPIO 20
- Row 3: GPIO 21
- Row 4: GPIO 26

Columns:

- Column 1: GPIO 8
- Column 2: GPIO 7
- Column 3: GPIO 1
- Column 4: GPIO 12

## Default Access Codes

Each tray is opened by a fixed 4-digit code:

- Tray 1: `1234`
- Tray 2: `5050`
- Tray 3: `0000`
- Tray 4: `1515`

If four digits are entered and the code does not match any of the values above, the LCD shows a wrong password message and the input resets.

## How It Works

When the program starts, it briefly runs a startup sequence and then registers a keypad handler. Every key press is appended to the current password buffer and shown on the LCD. Once a valid 4-digit code is detected, the corresponding tray output is activated for about 10 seconds and then turned off again.

## Running the Project

1. Connect the keypad, LCD, and tray outputs to the Raspberry Pi using the pin mapping above.
2. Install the Python dependencies.
3. Run the script:

```bash
python3 ApartiBot.py
```

## Notes

- The project depends on Raspberry Pi GPIO access, so it must be run on a compatible Raspberry Pi environment.
- Make sure the connected hardware is wired correctly before powering the outputs.
- If you change the GPIO wiring, update the pin numbers in `ApartiBot.py` accordingly.

## Project Goal

ApartiBot is intended as a simple physical access-control prototype for multiple compartments or trays. It can be adapted for secure parcel delivery, smart storage, or similar embedded hardware projects.
