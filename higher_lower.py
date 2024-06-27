# Import the art logo
from replit import clear
import art

print(art.logo)
# Import the game data
import game_data

# Create a function to randomly select a dictionary from the list
import random

def select_celebrity():
  return random.choice(game_data.data)

# Create a function to compare the follower count of the two celebrities
def compare_followers(celebrity_a, celebrity_b):
  if celebrity_a['follower_count'] > celebrity_b['follower_count']:
    return 'A'
  else:
    return 'B'

score = 0
celebrity_2 = select_celebrity()
continue_game = True
while continue_game:

  # Make celebrity B become the next celebrity A
  # Save the selected celebrity into variables
  celebrity_1 = celebrity_2
  celebrity_2 = select_celebrity()

  if celebrity_1 == celebrity_2:
    celebrity_2 = select_celebrity()
  
  print('Compare A: ' + celebrity_1['name'] + ', a ' + celebrity_1['description'] + ', from ' + celebrity_1['country'])
  print(art.vs)
  print('Against B: ' + celebrity_2['name'] + ', a ' + celebrity_2['description'] + ', from ' + celebrity_2['country'])
  
  answer = input('Who has more followers? Type "A" or "B": ').upper()
  
  correct_answer = compare_followers(celebrity_1, celebrity_2)
  
  if answer != correct_answer:
    clear()
    print(art.logo)
    print(f"Sorry that's wrong. Final score: {score}")
    continue_game = False
  else:
    clear()
    print(art.logo)
    score += 1
    print(f"You're right! Current score: {score}")
