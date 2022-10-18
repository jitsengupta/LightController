from time import sleep
import RPi.GPIO as GPIO

"""
The Light base class - just an LED controlled by a digital IO
Pin. Save the pin in an instance variable
"""
class Light:
    # Light constructor - save the pin and set it to OUTPUT mode
    def __init__(self, pin):
        print("Light: constructor")
        self._pin = pin
        GPIO.setup(self._pin, GPIO.OUT)

    # on: Turn the light on
    def on(self):
        print("Light: turning on pin {self._pin}")
        GPIO.output(self._pin, True)

    def off(self):
        print("Light: turning off pin {self._pin}")
        GPIO.output(self._pin, False)

"""
The Dimmable Light subclass - will have the standard on off methods
and in addition will have the ability to set brightness
"""
class DimLight(Light):
    # Dimmable light constructor
    def __init__(self, pin):
        print("Dimmable light constructor")
        super().__init__(pin)
        self._pwm = GPIO.PWM(pin, 100)

    # Turn on - full brightness
    def on(self):
        print("Dimlight: turn on (full brightness)")
        self.setBrightness(100)

    # Turn off - 0 brightness
    def off(self):
        print("Dimlight - turn off (brightness 0)")
        self.setBrightness(0)

    # Set brightness to a specific level
    def setBrightness(self, brightness):
        print("Dimlight: setting brightness to {brightness}")
        self._pwm.start(brightness)

    # Do a quick demo of going up and down full brightness levels
    # Here it is better to use ChangeDutyCycle
    def upDown(self):
        print("Dimlight: do an up-down demo")
        dc = 0
        self._pwm.start(dc)
        for i in range (0, 10):
            dc += 10
            self._pwm.ChangeDutyCycle(dc)
            sleep(0.2)

        for i in range (0, 10):
            dc -= 10
            self._pwm.ChangeDutyCycle(dc)
            sleep(0.2)
        self._pwm.stop()
