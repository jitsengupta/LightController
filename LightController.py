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
        print(f"LightController: add a component {comp}")
        self._components.append(comp)
        
    # Just a simple test application for running all components
    # Obviously, this assumes that all components respond to run()
    def runAll(self, times=2):
        print(f"lightController: Demo run all internal components {times} times")
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
    
# The entry point of the application. 
# Remember every Python file can have its own entry point, which is
# a great way to test the class(es) in that file. 
# So our test applciation creates an instance of our LightController class,
# Adds a couple of composite lights, then runs all the lights
# before turning them off

if __name__ == "__main__":
    mycontroller = LightController()

    mycontroller.addComponent(TrafficLight(Light("green", 6), Light("yellow", 0), Light("red", 5)))
    mycontroller.addComponent(Pixel(DimLight("R", 19), DimLight("G", 13), DimLight("B", 12)))
    
    mycontroller.runAll()
    mycontroller.off()

