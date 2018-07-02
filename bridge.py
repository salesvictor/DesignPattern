from abc import ABCMeta, abstractmethod


class DrawingAPI(metaclass=ABCMeta):
  @abstractmethod
  def draw_shape(self, shape):
    pass

class Shape(metaclass=ABCMeta):
  def __init__(self, drawing_api):
    self.drawing_api = drawing_api

  def draw(self):
    return self.drawing_api.draw_shape(self)

  @abstractmethod
  def linear_resize(self, fold):
    pass

class VectorizedDrawingAPI(DrawingAPI):
  def draw_shape(self, shape):
    return (f'Drawing vectorized {shape.description}'
            f' at {shape.x, shape.y} with'
            f' {shape.characteristic} = {shape.characteristic_val}')

class PNGDrawingAPI(DrawingAPI):
  def draw_shape(self, shape):
    return (f'Drawing {shape.description} in a PNG'
            f' at {shape.x, shape.y} with'
            f' {shape.characteristic} = {shape.characteristic_val}')
 
class Circle(Shape):
  def __init__(self, x, y, radius, drawing_api):
    self.description = 'circle'
    self.x = x
    self.y = y
    self.characteristic = 'radius'
    self.characteristic_val = radius
    super().__init__(drawing_api)
  
  def linear_resize(self, fold):
    self.characteristic_val = self.characteristic_val * fold

class Square(Shape):
  def __init__(self, x, y, side, drawing_api):
    self.description = 'square'
    self.x = x
    self.y = y
    self.characteristic = 'area'
    self.characteristic_val = side ** 2
    super().__init__(drawing_api)
  
  def linear_resize(self, fold):
    self.characteristic_val *= fold ** 2


def main():
  VAPI = VectorizedDrawingAPI()
  PNGAPI = PNGDrawingAPI()

  shapes = []

  vectorized_circle = Circle(1, 1, 5, VAPI)
  shapes.append(vectorized_circle)

  png_circle = Circle(0, 0, 3, PNGAPI)
  shapes.append(png_circle)

  vectorized_square = Square(2, 3, 5, VAPI)
  shapes.append(vectorized_square)

  png_square = Square(7, 8, 2, PNGAPI)
  shapes.append(png_square)

  for shape in shapes:
    print(shape.draw())

  print()

  for shape in shapes:
    shape.linear_resize(2)
    print(shape.draw())

if __name__ == '__main__':
  main()
