## Using Arduino 

To set up the environment in the Arduino IDE, follow these steps:
1. Go to "Library Manager".
   
<img src="../../images/library.png" alt="Library Manager" width="50%">

2. Install the available version of **Adafruit MAX1704X**.

<img src="../../images/install.png" alt="Install" width="20%">

Download the basic test code for connection:

<div style="text-align: center;">
    <a href="../../Software/MAX17048_basic/MAX17048_basic.ino" download="MAX17048_basic.ino">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            MAX17048_basic.ino
        </button>
    </a>
</div>

It is recommended to use the [DualMCU board]() for utilizing the JTAG connectors with the QWIIC method. The implementation code is for this board, but you can adapt the code to other compatible boards.
<div align="center">

<img src="../..//images/board1.jpg" alt="Connections" width="60%">

</div>

View the data through the serial monitor.
<div align="center">

![Serial Monitor](../../images/serial_monitor.png)

</div>