from Enemy import *

zombie = Enemy(type_of_enemy='Small Zombie', health_points=20, attack_damage=100)


print(zombie.talk())
print(zombie.walk_forward())
print(zombie.attack())