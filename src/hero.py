from weapon import *

class Hero:
  def __init__(self, health_points = 10, attack_damage = 1):
    self.health_points = health_points
    self.attack_damage = attack_damage
    self.is_weapon_equipped = False
    self.weapon: Weapon = None

  def talk(self):
    print(f'**Heroic Voice** I will defeat you!')
  
  def equip_weapon(self):
    if self.weapon is not None and not self.is_weapon_equipped:
      self.attack_damage += self.weapon.attack_increase
      self.is_weapon_equipped = True

  def attack(self):
    print(f'Hero is attacking for {self.attack_damage} damage!')