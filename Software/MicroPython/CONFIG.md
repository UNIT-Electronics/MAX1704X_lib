# Using MicroPython

This code has been tested on the RP2040 microcontroller of the [DualMCU]() board.


## Method of Use

To set up, download the library and save it onto the microcontroller. When using Thonny, ensure it is saved with the name `max1704x.py`.

<div style="text-align: center;">
    <a href="./example.zip" download="example.zip">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            example.zip
        </button>
    </a>
</div>

The `Test.py` code outlines the primary usage and any special instructions. It's essential to execute this code on the RP2040 board.

Quick test: Copy this code and run it using Thonny:

<img src="../../images/qwiic.png" style="display: block; margin-left: auto; margin-right: auto; width: 50%;">


```python
from max1704x import max1704x

mi_sensor = max1704x(sda_pin=12, scl_pin=13)

print("I2C address of the sensor:", mi_sensor.address())

mi_sensor.quickStart()
```

This version is adaptable to other boards, with a focus on close implementation.

