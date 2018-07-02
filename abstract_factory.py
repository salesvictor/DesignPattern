from abc import ABCMeta, abstractmethod

class PetShop(metaclass=ABCMeta):
  def __init__(self):
    self.dog = self._get_dog()

  @abstractmethod
  def _get_dog(self):
    pass

  def description(self):
    dog_status = self.dog.status()
    return f'PetShop that lefts your dogs {dog_status}.'

class Dog(metaclass=ABCMeta):
  @abstractmethod
  def status(self):
    pass

class GoodPetShop(PetShop):
  def _get_dog(self):
    return CleanDog()

class BadPetShop(PetShop):
  def _get_dog(self):
    return DirtyDog()

class CleanDog(Dog):
  def status(self):
    return 'clean'

class DirtyDog(Dog):
  def status(self):
    return 'dirty'


def main():
  pet_shop_a = GoodPetShop()
  pet_shop_b = GoodPetShop()
  pet_shop_c = BadPetShop()

  print(f'PetShop A: {pet_shop_a.description()}')
  print(f'PetShop B: {pet_shop_b.description()}')
  print(f'PetShop C: {pet_shop_c.description()}')

if __name__ == "__main__":
  main()
