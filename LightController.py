# RPi.GPIO is the Python library to use GPIO in Python on a Raspberry Pi
# This is the more object-oriented library - do not use the old gpiozero
# since it is a bit outdated, and not very OO-friendly.

# Most new Raspberry Pis should already have it installed, in case it
# isn't, you can run 
# sudo apt install 
import RPi.GPIO as GPIO
from CompositeLights import TrafficLight, Pixel
from Lights import Light, DimLight

"""
The base LightController class - the main application class for
running this application. It is possible to create a main entry 
point in any file in Python. So ensure you are running this one
to run the main application.
"""
class LightController:

    # The Constructor - set up the GPIO and the components array
    def __init__(self):
        print("LightController: initializer")
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self._components = []

    # Add a new component to the internal components array
    def addComponent(self, comp):
        print("LightController: add a component {comp}")
        self._components.append(comp)
        
    # Just a simple test application for running all components
    # Obviously, this assumes that all components respond to run()
    def runAll(self, times=2):
        print("lightController: Demo run all internal components {times} times")
        for c in self._components:
            for i in range(0,times):
                c.run()

    # Turn on all components 
    def on(self):
        print("LightController: turn all componets on")
        for c in self._components:
            c.on()

    # Turn off all componets
    def off(self):
        print("LightController: Turn off all components")
        for c in self._components:
            c.off()
        GPIO.cleanup()
    
if __name__ == "__main__":
    mycontroller = LightController()

    mycontroller.addComponent(TrafficLight(Light(6), Light(0), Light(5)))
    mycontroller.addComponent(Pixel(DimLight(19), DimLight(13), DimLight(12)))
    
    mycontroller.runAll()
    mycontroller.off()

