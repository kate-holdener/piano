# libraries for controlling lights

class LightController:
    DOWN = 144

    def __init__(self, api, color_on, color_off):
        self.api = api
        self.num_lights = api.get_num_lights()
        # state of the lights
        self.color_on = color_on
        self.color_off = color_off
        self.next_light = 0
        self.prev_light = -1

    def set_next(self, color):
        self.api.set_light(self.next_light, color)
        self.next_light+=1

    def set_previous(self, color):
        if self.prev_light >= 0:
           self.api.set_light(self.prev_light, color)
        self.prev_light+=1

    def update_colors(self, state):
        if state == LightController.DOWN:
            self.set_next(self.color_on)
            self.set_previous(self.color_off)
