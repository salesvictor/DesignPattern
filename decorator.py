from abc import ABCMeta, abstractmethod

class Weapon(metaclass=ABCMeta):
  @abstractmethod
  def description():
    pass

class WeaponAttachments(Weapon, metaclass=ABCMeta):
  def __init__(self, weapon):
    self._weapon = weapon

  @abstractmethod
  def description(self):
    pass

class AssaultRifle(Weapon):
  def description(self):
    return 'This is an assault rifle that fires'

class Scope(WeaponAttachments):
  def description(self):
    return self._weapon.description() + ' and has a scope'

class ExtendedMagazine(WeaponAttachments):
  def description(self):
    return self._weapon.description() + ' and has an extended magazine with 60 rounds'


def main():
  rifle1 = AssaultRifle()
  print(f'Rifle 1: {rifle1.description()}')

  rifle2 = Scope(rifle1)
  print(f'\nRifle 2: {rifle2.description()}')

  rifle3 = ExtendedMagazine(rifle2)
  print(f'\nRifle 3: {rifle3.description()}')
  print(f'\nRifle 1: {rifle1.description()}')

  rifle4 = ExtendedMagazine(rifle1)
  print(f'\nRifle 4: {rifle4.description()}')


if __name__ == '__main__':
  main()
