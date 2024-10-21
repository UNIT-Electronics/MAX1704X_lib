from max1704x import max1704x

# Initialize max17043/max17048 with the pins

# ESP32
# _id=-1
# SDA=21
# SCK=22

# RP2040
_id=0
SDA=12
SCK=13
my_sensor = max1704x(_id, sda_pin=SDA, scl_pin=SCK)

# Get the I2C address of the sensor
print("I2C address of the sensor:", my_sensor.address())

# Get the version of the max1704x module
print("Module version:", my_sensor.getVersion())

# Get the remaining voltage in the cell
print("Remaining cell voltage (V):", my_sensor.getVCell())

# Get the state of charge
print("State of charge (%):", my_sensor.getSoc())

# Get the compensation value
print("Compensation value:", my_sensor.getCompensateValue())

# Get the alert threshold
print("Alert threshold (%):", my_sensor.getAlertThreshold())

# Check if the sensor is in alert
print("Is in alert?:", "Yes" if my_sensor.inAlert() else "No")

# Perform a quick start reset of the sensor
my_sensor.quickStart()
