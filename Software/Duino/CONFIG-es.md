## Usando Arduino

Para configurar el entorno en el Arduino IDE, siga estos pasos:
1. Vaya a "Gestor de bibliotecas".

<img src="../../images/library.png" alt="Gestor de bibliotecas" width="50%">

2. Instale la versión disponible de **Adafruit MAX1704X**.

<img src="../../images/install.png" alt="Instalar" width="20%">

Descargue el código de prueba básico para la conexión:

<div style="text-align: center;">
    <a href="../../Software/MAX17048_basic/MAX17048_basic.ino" download="MAX17048_basic.ino">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            MAX17048_basic.ino
        </button>
    </a>
</div>

Se recomienda utilizar la [placa DualMCU]() para utilizar los conectores JTAG con el método QWIIC. El código de implementación es para esta placa, pero puede adaptar el código a otras placas compatibles.
<div align="center">

<img src="../../images/board1.jpg" alt="Conexiones" width="60%">

</div>

Vea los datos a través del monitor serie.
<div align="center">

![Monitor Serie](../../images/serial_monitor.png)

</div>