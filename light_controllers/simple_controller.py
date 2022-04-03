from .light_controller import LightController
class SimpleController(LightController):
    """
    Changes lights on each key down event such that the next
    light gets set to the ON color and the previous light that 
    was set to the ON color is set to the OFF color. When the
    strand runs out of lights, the *next* light is the first light
    in the strand, simulating a circular light strand.
    """
    def process_event(self, event):
        self.update_colors(event.is_down())
