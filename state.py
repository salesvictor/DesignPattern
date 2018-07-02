from abc import ABC, abstractmethod

class StateMachine:
  def __init__(self):
    self._state = S1()

  def set_state(self, state):
    self._state = state

  def action(self):
    self._state.action(self)

class S1:
  class __Singleton:
    def action(self, machine):
      print('Doing action with state S1')
      machine.set_state(S2())

  instance = None
  
  def __init__(self):
    if not S1.instance:
      S1.instance = S1.__Singleton()

  def __getattr__(self, name):
    return getattr(S1.instance, name)

class S2:
  class __Singleton:
    def action(self, machine):
      print('Doing action with state S2')
      machine.set_state(S3())

  instance = None
  
  def __init__(self):
    if not S2.instance:
      S2.instance = S2.__Singleton()

  def __getattr__(self, name):
    return getattr(S2.instance, name)

class S3:
  class __Singleton:
    def action(self, machine):
      print('Doing action with state S3')
      machine.set_state(S1())

  instance = None
  
  def __init__(self):
    if not S3.instance:
      S3.instance = S3.__Singleton()

  def __getattr__(self, name):
    return getattr(S3.instance, name)


def main():
  machine = StateMachine()
  for i in range(10):
    machine.action()

if __name__ == "__main__":
  main()
