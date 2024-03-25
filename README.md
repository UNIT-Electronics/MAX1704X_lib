# MAX1704X

El control del circuito integrado MAX1704X mediante Arduino se lleva a cabo a través de la comunicación I2C. En este repositorio, encontrarás ejemplos que ilustran la comunicación, permitiéndote obtener información como el voltaje de la batería, el porcentaje de carga, y el valor de carga o descarga.

<div align="center">

![Version 1.0](https://img.shields.io/badge/version-1.0-green)
![Review 0.1](https://img.shields.io/badge/review-0.1-blue)

</div>

<div align="center">

<img src="./images/image.png" alt="Diagrama de bloques vista reversa" width="300" height="200">
<img src="./images/front.png" alt="Diagrama de bloques vista frontal" width="300" height="200">

</div>

## Configuración del entorno

Para configurar el entorno en Arduino IDE, sigue estos pasos:

1. Ve a "Administrar bibliotecas".
   
<img src="./images/library.png" alt="library" width="50%">

2. Instala la versión disponible de **Adafruit MAX1704X**.

<img src="./images/install.png" alt="Install" width="20%">

Descarga el código básico de prueba para la conexión:


<div style="text-align: center;">
    <a href="./Software/MAX17048_basic/MAX17048_basic.ino" download="MAX17048_basic.ino">
        <button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">
            MAX17048_basic.ino
        </button>
    </a>
</div>


## Conexiones

Recomendamos la conexión a través del conector rápido QWIIC.

<div align="center">

<img src="./images/board1.jpg" alt="Conexiones" width="60%">

</div>

## Implementación

Visualiza la lectura de los datos en el Monitor Serie.

<div align="center">

![Monitor Serie](./images/serial_monitor.png)

</div>

<h1>Créditos y Referencias</h1>

<a href="https://github.com/adafruit/Adafruit_MAX1704X/tree/main">Adafruit_MAX1704X</a>
