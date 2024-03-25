"""
Descripción: Esta libreria funciona para la lectura de carateruisticas del la tarjeta de carga, comado como referencia
{Andre Peeters 2017/10/31}<https://github.com/andrethemac/max17043.py/tree/master>
Autor: CesarBautista
Fecha de creación: 25 de Marzo de 2024
Fecha de modificación:
Versión: 1.0
Dependencias: binascii, machine
"""
from machine import Pin, I2C
import binascii

class Max1704x:
    REGISTER_VCELL = const(0X02)
    REGISTER_SOC = const(0X04)
    REGISTER_MODE = const(0X06)
    REGISTER_VERSION = const(0X08)
    REGISTER_CONFIG = const(0X0C)
    REGISTER_COMMAND = const(0XFE)

    def __init__(self, sda_pin=12, scl_pin=13):
        self.sda_pin = sda_pin
        self.scl_pin = scl_pin
        self.i2c = I2C(0, sda=Pin(self.sda_pin), scl=Pin(self.scl_pin))
        self.max1704xAddress = self.i2c.scan()[0]

    def __str__(self):
        rs  = "La dirección I2C es {}\n".format(self.max1704xAddress)
        rs += "Los pines I2C son SDA: {} y SCL: {}\n".format(self.sda_pin, self.scl_pin)
        rs += "La versión es {}\n".format(self.get_version())
        rs += "VCell es {} V\n".format(self.get_vcell())
        rs += "Compensatevalue es {}\n".format(self.get_compensate_value())
        rs += "El umbral de alerta es {} %\n".format(self.get_alert_threshold())
        rs += "¿Está en alerta? {}\n".format(self.in_alert())
        return rs

    def address(self):
        return self.max1704xAddress

    def reset(self):
        self.__write_register(REGISTER_COMMAND, binascii.unhexlify('0054'))

    def get_vcell(self):
        buf = self.__read_register(REGISTER_VCELL)
        return (buf[0] << 4 | buf[1] >> 4) / 1000.0

    def get_soc(self):
        buf = self.__read_register(REGISTER_SOC)
        return (buf[0] + (buf[1] / 256.0))

    def get_version(self):
        buf = self.__read_register(REGISTER_VERSION)
        return (buf[0] << 8) | (buf[1])

    def get_compensate_value(self):
        return self.__read_config_register()[0]

    def get_alert_threshold(self):
        return (32 - (self.__read_config_register()[1] & 0x1f))

    def set_alert_threshold(self, threshold):
        self.threshold = 32 - threshold if threshold < 32 else 32
        buf = self.__read_config_register()
        buf[1] = (buf[1] & 0xE0) | self.threshold
        self.__write_config_register(buf)

    def in_alert(self):
        return (self.__read_config_register())[1] & 0x20

    def clear_alert(self):
        self.__read_config_register()

    def quick_start(self):
        self.__write_register(REGISTER_MODE, binascii.unhexlify('4000'))

    def __read_register(self, address):
        return self.i2c.readfrom_mem(self.max1704xAddress, address, 2)

    def __read_config_register(self):
        return self.__read_register(REGISTER_CONFIG)

    def __write_register(self, address, buf):
        self.i2c.writeto_mem(self.max1704xAddress, address, buf)

    def __write_config_register(self, buf):
        self.__write_register(REGISTER_CONFIG, buf)

    def deinit(self):
        self.i2c.deinit()
