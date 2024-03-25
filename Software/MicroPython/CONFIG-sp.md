# Usando MicroPython

Este código ha sido probado en el microcontrolador RP2040 de la placa [DualMCU]().

## Método de Uso

Para configurar, descarga la biblioteca y guárdala en el microcontrolador. Cuando uses Thonny, asegúrate de guardarla con el nombre `max1704x.py`.

<div style="text-align: center;">
    <a href="./example.zip" download="example.zip">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            example.zip
        </button>
    </a>
</div>

El código `Test.py` describe el uso principal y cualquier instrucción especial. Es esencial ejecutar este código en la placa RP2040.

Prueba rápida: Copia este código y ejecútalo usando Thonny:

<img src="../../images/qwiic.png" style="display: block; margin-left: auto; margin-right: auto; width: 50%;">


```python
from max1704x import max1704x

mi_sensor = max1704x(sda_pin=12, scl_pin=13)

print("Dirección I2C del sensor:", mi_sensor.address())

mi_sensor.quickStart()
```

Esta versión es adaptable a otras placas, con un enfoque en la implementación cercana.

