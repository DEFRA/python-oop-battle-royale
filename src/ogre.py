from enemy import *
import random

class Ogre(Enemy):
  def __init__(self, health_points = 20, attack_damage = 3):
    super().__init__("Ogre", health_points, attack_damage)

  def talk(self):
    print(f'**Rooooooar**')
  
  def special_ability(self):
    did_special_ability_work = random.random() < 0.20
    if did_special_ability_work:
      self.attack_damage += 4
      print(f'{self.get_type_of_enemy()} has increased attack damage by 4!')