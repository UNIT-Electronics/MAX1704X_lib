from max1704x import max1704x

# Inicializar el objeto max17043  y max17048 con los pines 12 y 13
mi_sensor = max1704x(sda_pin=12, scl_pin=13)

# Obtener la dirección I2C del sensor
print("Dirección I2C del sensor:", mi_sensor.address())

# Obtener la versión del módulo max1704x
print("Versión del módulo:", mi_sensor.getVersion())

# Obtener el voltaje restante en la celda
print("Voltaje restante en la celda (V):", mi_sensor.getVCell())

# Obtener el estado de carga
print("Estado de carga (%):", mi_sensor.getSoc())

# Obtener el valor de compensación
print("Valor de compensación:", mi_sensor.getCompensateValue())

# Obtener el umbral de alerta
print("Umbral de alerta (%):", mi_sensor.getAlertThreshold())

# Comprobar si el sensor está en alerta
print("¿Está en alerta?:", "Sí" if mi_sensor.inAlert() else "No")

# Realizar un reinicio rápido del sensor
mi_sensor.quickStart()

