from zombie import *
from ogre import *
from hero import *

def battle(e1: Enemy, e2: Enemy):

  print('----------------------')
  print(f'{e1.get_type_of_enemy()} Ready!!!!')
  e1.talk()
  print('----------------------')
  print(f'{e2.get_type_of_enemy()} Ready!!!!')
  e2.talk()
  print('----------------------')
  print('     ## FIGHT ##      ')
  print('----------------------')

  while e1.health_points > 0 and e2.health_points > 0:
    e1.special_ability()
    e2.special_ability()
    print(f'{e1.get_type_of_enemy()} has {e1.health_points} health points left!')
    print(f'{e2.get_type_of_enemy()} has {e2.health_points} health points left!')
    e2.attack()
    e1.health_points -= e2.attack_damage
    e1.attack()
    e2.health_points -= e1.attack_damage
    print('----------------------')

  if(e1.health_points > 0):
    print(f'{e1.get_type_of_enemy()} has won!')
  else:
    print(f'{e2.get_type_of_enemy()} has won!')
  
  print('----------------------')

def hero_battle(hero: Hero, enemy: Enemy):
  print('----------------------')
  print(f'Hero Ready!!!!')
  hero.talk()
  print('----------------------')
  print(f'{enemy.get_type_of_enemy()} Ready!!!!')
  enemy.talk()
  print('----------------------')
  print('     ## FIGHT ##      ')
  print('----------------------')

  while hero.health_points > 0 and enemy.health_points > 0:
    enemy.special_ability()
    print(f'Hero has {hero.health_points} health points left!')
    print(f'{enemy.get_type_of_enemy()} has {enemy.health_points} health points left!')
    enemy.attack()
    hero.health_points -= enemy.attack_damage
    hero.attack()
    enemy.health_points -= hero.attack_damage
    print('----------------------')

  if(hero.health_points > 0):
    print('Hero has won!')
  else:
    print(f'{enemy.get_type_of_enemy()} has won!')
  
  print('----------------------')


zombie = Zombie(10, 1)
# ogre = Ogre(20, 3)
# battle(zombie, ogre)

hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()
hero_battle(hero, zombie)