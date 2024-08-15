'''
We'll create a game with 2 fighters 
It goes 10 rounds
Every round, both fighters get a chance to enter a move (punch, kick, block)
    Block will mitigate damage by a random %

    Kick/Punch will reduce the health of the other opponent by random.randint() amount of damage

Game ends when one Fighter is KOed or round 10 is reached

Randomize what fighters move is executed first: random, 1 or 2 (unless a player blocked, because we have to mitigate that incoming damage)
'''

import random

class Fighter:
    def __init__(self):
        self.health = 100

    def attack(self, input):
        if input == 1:
            return random.randint(5, 15)
        elif input == 2:
            return random.randint(5, 25)
    
    def block(self, damage):
        return damage * (random.random())
    
class Game:
    def __init__(self):
        self.fighter_one = Fighter()
        self.fighter_two = Fighter()
        self.rounds = 0

        print(
            '''
                WELCOME TO FRIGHT FIGHT CLUB NIGHT
            '''
        )

    def start_game(self):
        while self.rounds < 10:
            # let fighters choose moves
            print('\n----------------------------------------------------------------------------------------------')
            print('Fighters! Choose your moves.')
            fighter_one_input = int(input('Fighter One! Choose: 1: Punch, 2: Kick, 3: Block (enter 1, 2, or 3): '))            
            fighter_two_input = int(input('Fighter Two! Choose: 1: Punch, 2: Kick, 3: Block (enter 1, 2, or 3): '))

            # Damage logic
            if fighter_one_input == 3:
                fighter_two_damage = self.fighter_two.attack(fighter_two_input)
                damage_to_fighter_one = fighter_two_damage - self.fighter_one.block(fighter_two_damage)

                self.fighter_one.health -= damage_to_fighter_one
            elif fighter_two_input == 3:
                fighter_one_damage = self.fighter_one.attack(fighter_one_input)
                damage_to_fighter_two = fighter_one_damage - self.fighter_two.block(fighter_one_damage)

                self.fighter_two.health -= damage_to_fighter_two
            else:
                fighter_goes_first = random.randint(1, 2)

                if fighter_goes_first == 1:
                    fighter_one_damage = self.fighter_one.attack(fighter_one_input)
                    self.fighter_two.health -= fighter_one_damage
                else:
                    fighter_two_damage = self.fighter_two.attack(fighter_two_input)
                    self.fighter_one.health -= fighter_two_damage

            print('\nCurrent fighter health:\n\tFighter One health: {fighter_one_health}.\n\tFighter Two health: {fighter_two_health}'.format(fighter_one_health=self.fighter_one.health, fighter_two_health=self.fighter_two.health))

            # Check health:
            if self.fighter_one.health <= 0:
                print('Fighter 2 has won!')
                return True
            elif self.fighter_two.health <= 0:
                print('Fighter 1 has won!')
                return True

        print('The game was a draw.')
        return False
    
game = Game()
game.start_game()
