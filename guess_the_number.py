#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from replit import clear

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def compare(user_answer, computer_answer,attempts):
  if user_answer == computer_answer:
    print('You win!')
  elif user_answer > computer_answer:
    print('Too high.')
    return attempts - 1
  elif user_answer < computer_answer:
    print('Too low.')
    return attempts - 1
    
def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

  if difficulty == 'easy':
    return EASY_ATTEMPTS
  elif difficulty == 'hard':
    return HARD_ATTEMPTS
  



def play_game():
  computer_choice = random.randint(1,100)
  
  print('Welcome to the Number Guessing Game!')
  print("I'm thinking of a number between 1 and 100.")
  
  attempts = set_difficulty()
  
  guess = 0
  while guess != computer_choice:
    print(f'You have {attempts} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))
    attempts = compare(guess,computer_choice,attempts)

    if attempts == 0:
      print('You lose.')
      break

    print('Guess again.')

restart_game = True

while restart_game:
  play_game()

  restart = input('Do you want to restart the game? Type "y" or "n": ')

  if restart == 'n':
    print('Bye!')
    break
  elif restart == 'y':
    clear()
