class Enemy:
    type_of_enemy: str
    health_points: int = 20
    attack_damage: int = 1

    def talk(self):
        print(f'I am a {self.type_of_enemy}. Be prepared to fight')
    
    def walk_forward(self):
        print(f'{self.type_of_enemy} move closer to you')

    def attack(self):
        print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage')