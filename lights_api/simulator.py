# importing the required libraries

from graphics import *

class Simulator():
   def __init__(self, numLights):
      self.lights=[]
      self.numLights = numLights
      self.win = GraphWin('Lights simulator', 600, 400)

      # creating a label widget
      # by default label will display at top left corner
      for i in range(self.numLights):
         point = Point(100+i*20, 100)
         circle = Circle(point, 10)
         circle.setOutline('black')
         circle.draw(self.win)
         self.lights.append(circle)

   def get_num_lights(self):
      return self.numLights

   def _set_one_light(self, light_index, color):
      self.lights[light_index].setFill(color_rgb(color[0],color[1],color[2]))

   def set_light(self, light_index, color):
      self._set_one_light(light_index, color)
      update()

   def set_all_lights(self, color):
      for i in range(self.numLights):
         self._set_one_light(i, color)
      update()

if __name__ == '__main__':
   simulator = Simulator(10)
   simulator.set_light(5, (255,0,0))
   simulator.set_all_lights((0,255,0))


