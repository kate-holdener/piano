from light_controller import rainbow_controller
from piano_lights import LightsFromPiano
from lights_api import simulator

api = simulator.Simulator(20)
lights_controller = rainbow_controller.RainbowController(api)
piano_input = LightsFromPiano()
piano_input.run(lights_controller)
