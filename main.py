#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
  no_of_attempts_left = 10
  print(f"You have {no_of_attempts_left} attempts remaining to guess the number.")
elif difficulty == 'hard':
  no_of_attempts_left = 5
  print(f"You have {no_of_attempts_left} attempts remaining to guess the number.")

user_guess = int(input("Make a guess: "))
actual_answer = random.randint(2,99)         # 1 and 100 not included 

def answer_is_wrong():     # Create function with docstring
  """check if user_guess not equal to actual_answer, will minus no_of_attempts_left"""
  while user_guess != actual_answer:
    ### METHOD 1: global no_of_attempts_left      # to modify global variable within local scope---> so that i can change the value of that global variable   (NOT GOOD METHOD)----> because you are modifying a global function within a local scope 
    global no_of_attempts_left
    no_of_attempts_left -= 1               # always minus 1 attempt when guess wrongly
    print(f"You have {no_of_attempts_left} attempts remaining to guess the number.")
    break       # So that i will only print the above statement once in each loop
    
    #INSTEAD, DO METHOD 2: Include parameter in function and use return of that variable(NOT SHOWN HERE)
    

flag_variable = False     # Create flag variable so i can exit while loop

while not flag_variable:          # while True 
  if user_guess < actual_answer: 
    print("Too low.")
    print("Guess again.")
    answer_is_wrong()                       # print number of attempts remaining
    if no_of_attempts_left == 0:        # scenario where no more attempts left
      print("You have run out of attempts and lost!")   
      break              # ends the program by exiting while loop
    user_guess = int(input("Make a guess: "))     # guess again 
    
  elif user_guess > actual_answer:
    print("Too high.")
    print("Guess again.")
    answer_is_wrong()                       # print number of attempts remaining
    if no_of_attempts_left == 0:        # scenario where no more attempts left
      print("You have run out of attempts and lost!")   
      break             # ends the program by exiting while loop
    user_guess = int(input("Make a guess: "))     # guess again
    
  elif user_guess == actual_answer:
    print(f"Congrats, you are correct! The number is {actual_answer}.")
    flag_variable = True            # ends the program 
  