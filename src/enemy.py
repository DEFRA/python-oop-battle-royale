class Enemy:

  def __init__(self, type_of_enemy, health_points = 10, attack_damage = 1):
    self.__type_of_enemy = type_of_enemy
    self.health_points = health_points
    self.attack_damage = attack_damage

  def get_type_of_enemy(self):
    return self.__type_of_enemy 

  def talk(self):
    print(f'I am an {self.__type_of_enemy}. Be prepared to fight!')

  def attack(self):
    print(f'{self.__type_of_enemy} is attacking for {self.attack_damage} damage!')

  def walk_forward(self):
    print(f'{self.__type_of_enemy} is walking forward!')

  def special_ability(self):
    print(f'{self.__type_of_enemy} has no special ability!')