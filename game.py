# building a game to practice/learn python .

# This is just a simple game that asks for your input from the user to choose from multiple choices.

import random # exactly what it says, generates random values

monsters = [
    {'name': 'didam', 'desc': 'the frog', 'health': 20, 'min_attack': 0,'max_attack':5},


  {'name':'Troll',
   'desc':'Just a troll\n'
          '---O----O---\n'
          '     /|    \n'
          '   ======    ',
   'health':100,
   'min_attack':11,
   'max_attack':13,},


  {'name':'Orc',
   'desc':'Just an Orc\n'
     '({  ^^^^^^^  }\n'
      '{ (X)   (X) } \n'
      '{     W     }\n'
      '{  <BOSS>   }',
   'health':120,
   'min_attack':10,
   'max_attack':15 },

  {'name':'Albatatis',
   'desc':'Albatatis, the world conquer\n'
      '|||||||||\n'
      '| +   +|\n'
      '|   -  | \n'
      '|E3E3E3|\n'
      '_______',
   'health':120,
   'min_attack':13,
   'max_attack':15},

]


def new_random(): # generates a random value between index 0 and the monsters list length
  return random.randint(0, len(monsters)-1) # start, end-1
def attack_random():
    return random.randint(monster['min_attack'], monster['max_attack']-1)#makes it more complex

game_running = True
start_game = input('Type gg to start the game:')

while game_running == True:
   new_round = True

   player = {'health' : 100, 'attack' : 10, 'heal' : 12}
   monster = monsters[new_random()]

   print('You encountered:', monster['desc'])

   while new_round == True:

       player_won = False
       monster_won = False

       if start_game == 'gg':
            print('*-*-*-' * 7)
            print('Choose your action')
            print('1.Attack')
            print('2.heal')
            print('5.run')
            print('9.quit')

       else:
           print('Come back later!')
           new_round = False
           game_running = False
           break # breaks the loop
         # part 2
       action = input()

       if action == '1':
           monster['health'] = monster['health'] - player['attack']
           if monster['health'] <= 0:
              player_won = True

           player['health'] = player['health'] - attack_random()
           if player['health'] <= 0:
               monster_won = True
           print('Attack!')
       elif action == '2':
           player['health'] = player['health'] + player['heal']
       elif action == '5':
           print('You managed to scape!\n\n') # \n just adds a new line to a string
           new_round = False
           break
       elif action == '9':
           print('Quiting!')
           new_round = False
           game_running = False
           break
       else:
           print('invalid selection')

       print('Monster HP: ', monster['health'])
       print('Player HP:', player['health'])

       if player_won == True or monster_won == True:
           if player_won == True:
             print('game ends, player won')
           else:
             print('game ends, monster won')

           new_round = False
