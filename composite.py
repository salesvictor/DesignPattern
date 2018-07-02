from abc import ABCMeta, abstractmethod

class ArithmeticExpression(metaclass=ABCMeta):
  @abstractmethod
  def evaluate(self):
    pass

  @abstractmethod
  def print(self):
    pass

class ExpressionComposite(ArithmeticExpression):
  def __init__(self, op, left, right):
    self._op = op
    self._left = left 
    self._right = right

  def evaluate(self):
    left_eval = self._left.evaluate()
    right_eval = self._right.evaluate()
    return eval(f'({left_eval} {self._op} {right_eval})')

  def print(self):
    left_print = self._left.print()
    right_print = self._right.print()
    return f'({left_print} {self._op} {right_print})'

class Leaf(ArithmeticExpression):
  def __init__(self, number):
    self._number = number

  def evaluate(self):
    return self._number

  def print(self):
    return self._number


def main():
  leaf5 = Leaf(5)
  leaf1 = Leaf(1)
  ex1 = ExpressionComposite('+', leaf5, leaf1)
  print(ex1.print())
  print(ex1.evaluate())
  print()

  leaf7 = Leaf(7)
  ex2 = ExpressionComposite('*', leaf7, ex1)
  print(ex2.print())
  print(ex2.evaluate())
  print()

  leaf42 = Leaf(42)
  ex3 = ExpressionComposite('//', leaf42, ex2)
  print(ex3.print())
  print(ex3.evaluate())

if __name__ == '__main__':
  main()
