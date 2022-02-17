from light_controller import simple_controller
from piano_lights import LightsFromPiano

lights_controller = simple_controller.SimpleController(5, (244,0,0), (0,0,255))
piano_input = LightsFromPiano()
piano_input.run(lights_controller)
