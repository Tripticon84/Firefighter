import RPi.GPIO as GPIO
import time

# GPIO setup -- pin 29 as moisture sensor input
# Sensor: GPIO 29
# Relay 1: GPIO 37
# Relay 2: GPIO 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.IN)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)

# Setup interval time and watering time in seconde
interval = 5
water = 2

try:
    while True:
        # Turn on sensor & allow settle
        (GPIO.output(38,True))
        time.sleep(1)
        # Check if dry, and if so open valve for watering time
        if (GPIO.input(29))==1:
            (GPIO.output(37, True))
            time.sleep(water)
            (GPIO.output(37, False))
        # Turn off sensor and wait for interval time
        (GPIO.output(38, False))
        time.sleep(interval)
  
finally:

    GPIO.cleanup()
