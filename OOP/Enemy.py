class Enemy:
    """
    Constructor
    "self" refers to the current class/object.
    """
    def __init__(self, type_of_enemy, health_points, attack_damage):
        # by adding __ the property will be set as private(Encapsulation the variable by using private)
        self.__type_of_enemy = type_of_enemy
        # these variable below will be set as Public(by default accessible) 
        self.health_points = health_points 
        self.attack_damage = attack_damage 

    def talk(self):
        print(f'I am a {self.__type_of_enemy}. Be prepared to fight')
    
    def walk_forward(self):
        print(f'{self.__type_of_enemy} move closer to you')

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')
    
    def get_type_of_enemy(self):
        return self.__type_of_enemy