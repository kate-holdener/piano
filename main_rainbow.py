from light_controller import rainbow_controller
from piano_lights import LightsFromPiano

lights_controller = rainbow_controller.RainbowController(50)
piano_input = LightsFromPiano()
piano_input.run(lights_controller)
