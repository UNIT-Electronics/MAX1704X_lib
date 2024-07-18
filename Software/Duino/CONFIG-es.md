## Usando Arduino

Para configurar el entorno en el Arduino IDE, siga estos pasos:
1. Vaya a "Gestor de bibliotecas".

<div align="center">

<img src="../../images/library.png" alt="Gestor de bibliotecas" width="50%">

</div>

2. Instale la versión disponible de **Adafruit MAX1704X**.

<div align="center">

<img src="../../images/install.png" alt="Instalar" width="20%">

</div>
Descargue el código de prueba básico para la conexión:


- [MAX17048_basic.ino](./MAX17048_basic/MAX17048_basic.ino)
- [MAX17048_advanced.ino](./MAX17048_advanced/MAX17048_advanced.ino)

Se recomienda utilizar la [placa DualMCU](https://uelectronics.com/producto/unit-dualmcu-esp32-rp2040-tarjeta-de-desarrollo/) para utilizar los conectores JTAG con el método QWIIC. El código de implementación es para esta placa, pero puede adaptar el código a otras placas compatibles.

<div align="center">

<img src="../../images/board1.jpg" alt="Conexiones" width="60%">

</div>

Vea los datos a través del monitor serie.
<div align="center">

![Monitor Serie](../../images/serial_monitor.png)

</div>

---
⌨️ con ❤️ por [UNIT-Electronics](https://github.com/UNIT-Electronics) 😊