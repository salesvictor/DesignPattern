class CommTower:
  def __init__(self, name):
    self.name = name
    self._airplanes = set()
    self._airports = set()

  def add_airplane(self, airplane):
    self._airplanes.add(airplane)

  def add_airport(self, airport):
    self._airports.add(airport)

  def remove_airplane(self, airplane):
    self._airplanes.discard(airplane)

  def remove_airport(self, airport):
    self._airports.discard(airport)

  def get_availiable(self):
    available_airport = None
    for airport in self._airports:
      if not available_airport and airport.is_available():
        available_airport = airport
    
    if not available_airport:
      print(f'CommTower {self.name}: Landing denied, stand by')
    else:
      print(f'CommTower {self.name}: Proceed to land on {available_airport.name}')

    return available_airport

class Airplane:
  def __init__(self, name, tower):
    self.name = name
    self._tower = tower

    tower.add_airplane(self)

  def request_landing(self):
    print(f'Airplane {self.name}: Requesting landing to {self._tower.name}')
    airport = self._tower.get_availiable()

    if airport:
      print(f'Airplane {self.name}: Landing on {airport.name}')

    else:
      print(f'Airplane {self.name}: Standing by')

class Airport:
  def __init__(self, name, tower, full):
    self.name = name
    self._tower = tower
    self.full = full

    tower.add_airport(self)

  def is_available(self):
    return  not self.full


def main():
  tower = CommTower('Charlie')

  airplane = Airplane('Boeing 737', tower)
  airport1 = Airport('Guarulhos', tower, True)

  airplane.request_landing()
  
  airport2 = Airport('Congonhas', tower, False)

  airplane.request_landing()

if __name__ == '__main__':
  main()
