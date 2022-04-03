from entity.midi_event import Event
from light_controllers.simple_controller import SimpleController

class Api:
    def __init__(self, num_lights):
        self.lights = [(-1,-1,-1)] * num_lights

    def get_num_lights(self):
        return len(self.lights)

    def set_light(self, index, color):
        self.lights[index] = color

def test_first_key_down():
    api = Api(10)
    down_event = Event(144, 45, 20, 1)
    simple_controller = SimpleController(api, (5,5,5), (1,1,1))
    simple_controller.process_event(down_event)
    assert api.lights[0] == (5,5,5)
    for color in api.lights[1:]:
        assert color == (-1,-1,-1)

def test_full_strand():
    api = Api(2)
    down_event = Event(144, 45, 20, 1)
    simple_controller = SimpleController(api, (5,5,5), (1,1,1))
    simple_controller.process_event(down_event)
    simple_controller.process_event(down_event)
    assert api.lights[1] == (5,5,5)
    assert api.lights[0] == (1,1,1)
