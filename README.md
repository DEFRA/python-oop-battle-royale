# Python - Object Oriented Programming

Object Oriented Programming (OOP) - is a programming paradigm based on the concept of "objects", which can contain data and code.

This is an example python app showing the use of OOP, along with a simple guide.

## Objects

- **Car**: A car has attributes (color, model, speed) and behaviors (drive, stop, honk), an object has attributes (data) and methods (functions).

```python
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self):
        print(f"The {self.color} {self.model} is driving.")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")

my_car = Car("red", "Ford")
my_car.drive()
my_car.stop()
```

## 4 pillars

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

## Abstraction

- **Driving a Car**: When you drive a car, you interact with the steering wheel, pedals, and gear shift. You don't need to understand the complex mechanics of the engine, transmission, or braking system to drive the car.

Abstraction hides the implementation details and only shows the necessary features to the user.

``` python
class Enemy:

  def __init__(self, type_of_enemy):
        self.type_of_enemy = type_of_enemy

  def talk(self):
    print(f'I am an {self.type_of_enemy}. Be prepared to fight!')

  def attack(self):
    print(f'{self.type_of_enemy} is attacking!')

```

``` python
zombie = Enemy("zombie")
zombie.talk()
zombie.attack()
```

## Encapsulation

- **A capsule that contains medicine**: The capsule hides the medicine inside it, protecting it from the external environment and ensuring that it is only released when needed.

Encapsulation hides the internal state of an object and only exposes a controlled interface for interacting with that state.

``` python
class Enemy:

  def __init__(self, type_of_enemy, health_points = 10, attack_damage = 1):
    self.type_of_enemy = type_of_enemy
    self.health_points = health_points
    self.attack_damage = attack_damage
```

Each of the 3 varibles (`type_of_enemy`, `health_points` and `attack_damage`) are "public" and can be overidden when instantiated eg.

``` python
zombie = Enemy('Zombie')
zombie.type_of_enemy = 'Orc'
```

To make the "public" attributes private we use double underscore eg `__type_of_enemy`

We can then user `getters` and `setters`

``` python
class Enemy:

  def __init__(self, type_of_enemy, health_points = 10, attack_damage = 1):
    self.__type_of_enemy = type_of_enemy
    self.health_points = health_points
    self.attack_damage = attack_damage
  
  def get_type_of_enemy(self):
    return self.__type_of_enemy 

  def set_type_of_enemy(self, type_of_enemy ):
    self.__type_of_enemy = type_of_enemy 
```

To prohibit the use of overriding of `type_of_enemy` with a setter, we can just remove the `setter`

To return the `type_of_enemy`:

``` python
zombie = Zombie(10, 1)
print(f'Type of enemy: {zombie.get_type_of_enemy()}')
```

## Inheritance

- **Family tree**: Just as children inherit traits and behaviors from their parents, a class can inherit attributes and methods from another class.

Enemy is the parent class and other classes can acquire its properites.

``` python
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
```

The `Zombie` class inherits all the attributes and methods from the parent class of `Enemy`. Within the child `Zombie` class we can then add additional attributes that are only specific to a zombie eg. `spread_infection`. We can also override the methods eg `talk`.

``` python
class Zombie(Enemy):
  def __init__(self, health_points = 10, attack_damage = 1):
    super().__init__("Zombie", health_points, attack_damage)

  def talk(self):
    print(f'**Grumbling**')

  def spread_infection(self):
    print(f'{self.get_type_of_enemy()} is spreading the infection!')
```

## Difference between `self` and `super`

- **`self`**: Refers to the instance of the class. It is used to access variables and methods that belong to the instance. When you define methods in a class, you use `self` to refer to the instance that calls the method.

- **`super`**: Refers to the parent class. It is used to call methods and access properties of the parent class. This is particularly useful in inheritance when you want to extend or modify the behavior of the parent class.

## Polymorphism

- **Universal control**: A universal remote can control various devices (TV, DVD player, sound system) using the same set of buttons. Each device responds differently to the same button press.

Polymorphism allows objects of different classes to be treated as objects of a common superclass. The same method can behave differently based on the object that it is acting upon.

- The `Enemy` class defines a common interface with the `attack` method.

- The `Zombie` and `Ogre` classes implement the `attack` and `talk` methods differently.

- The `attack()` and `talk()` functions can take any `Enemy` object and call its `attack` and `talk` method, demonstrating polymorphis

``` python
 def battle(e: Enemy):
   e.talk()
   e.attack()

 zombie = Zombie(10, 1)
 ogre = Ogre(30, 3)

 battle(zombie)
 battle(ogre)
```

Output

``` terminal
**Grumbling**
Zombie is attacking for 1 damage!
**Rooooooar**
Ogre is attacking for 3 damage!
```

## Composition

- **Building a Car**:  A car is composed of an engine, wheels, seats, and other components. Each part has its own functionality, and together they form a complete car.

Composition involves creating complex objects by combining simpler objects. This allows for more flexible and reusable code.

- The `Hero` class is composed of a `Weapon` object.
- The `Hero` class uses the `Weapon` object to increase its attack damage, demonstrating composition.

``` python
class Weapon:
    def __init__(self, name, attack_increase):
        self.name = name
        self.attack_increase = attack_increase

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
```

``` python
hero = Hero(10, 1)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()
```
