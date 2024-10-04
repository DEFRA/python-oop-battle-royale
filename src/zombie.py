from enemy import *
import random

class Zombie(Enemy):
  def __init__(self, health_points = 10, attack_damage = 1):
    super().__init__("Zombie", health_points, attack_damage)

  def talk(self):
    print(f'**Grumbling**')

  def spread_infection(self):
    print(f'{self.get_type_of_enemy()} is spreading the infection!')

  def special_ability(self):
    did_special_ability_work = random.random() < 0.50
    if did_special_ability_work:
      self.health_points += 2
      print(f'{self.get_type_of_enemy()} has increased health points by 2!')