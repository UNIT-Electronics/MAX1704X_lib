# Using MicroPython

This code has been tested on the RP2040 microcontroller of the [DualMCU](https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/) board.


## Method of Use

To set up, download the library and save it onto the microcontroller. When using Thonny, ensure it is saved with the name `max1704x.py`.

- [Library](./example/max1704x.py)

The `Test.py` code outlines the primary usage and any special instructions. It's essential to execute this code on the RP2040 board.

- [Test](./example/Test.py)

Quick test: Copy this code and run it using Thonny:

<div aling = "center">

<img src="../../images/qwiic.png" style="display: block; margin-left: auto; margin-right: auto; width: 50%;">

</div>

```python
from max1704x import max1704x

mi_sensor = max1704x(sda_pin=12, scl_pin=13)

print("I2C address of the sensor:", mi_sensor.address())

mi_sensor.quickStart()
```

This version is adaptable to other boards, with a focus on close implementation.


# MAX1704X Installation Guide Using MIP Library

> **Note:** Direct support for mip on RP2040 is not available. The `mip` library is utilized to install the `max1704x.py` library.

## Requirements
- ESP32 device
- Thonny IDE
- Wi-Fi credentials (SSID and Password)

## Installation Instructions

Follow the steps below to install the `max1704x.py` library:

### 1. Connect to Wi-Fi

Copy and run the code below in Thonny to connect your ESP32 to a Wi-Fi network:

```python
import mip
import network
import time

ssid = "your_ssid"
password = "your_password"

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    for _ in range(10):
        if wlan.isconnected():
            print('Connected to the Wi-Fi network')
            return wlan.ifconfig()[0]
        time.sleep(1)

    print('Could not connect to the Wi-Fi network')
    return None

ip_address = connect_wifi(ssid, password)
```
---
⌨️ with ❤️ from [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊