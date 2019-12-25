# building a game to practice/learn python .

# This is just a simple game that asks for your input from the user to choose from multiple choices.
player_health = 100
player_attack = 10
player_heal = 12

monster_health = 100
monster_attack = 13
game_running = True
start_game = input('Type gg to start the game:')

while game_running == True:
   new_round = True

   while new_round == True:

       player_won = False
       monster_won = False

       if start_game == 'gg':
            print('*-*-*-' * 7)
            print('Choose your action')
            print('1.Attack')
            print('2.heal')

       else:
           print('Come back later!')

       action = input()

       if action == '1':
           monster_health = monster_health - player_attack
           if monster_health <= 0:
               monster_won = True

           player_health = player_health - monster_attack
           if player_health <= 0:
               monster_won == True
           print('Attack!')
           print(monster_health)
           print(player_health)
       elif action == '2':
           player_health = player_health + player_heal
           print(monster_health)
           print(player_health)
       else:
           print('invalid selection')


       if player_won == True or monster_won == True:
           print('game ends')
           new_round = False

