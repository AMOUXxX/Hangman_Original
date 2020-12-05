from Data import words
from Data import logo
from Data import stages
from Function import start
import replit
import random


chosen_word = random.choice(words.word_choice)
chosen_word.lower()
chosen_word = list(chosen_word)

display= []
for blanks in chosen_word:
  display += "_"



def computer_game():
  replit.clear()
  blank = "_"
  Lives = 0
  used_letters = []
  end_game = False
  while end_game is False:
    print(display)
    print(stages.Hangman[Lives])
    print("Choose a letter : ")
    guess = input().lower()
    no_of_times = 0
    for letter in chosen_word:
      no_of_times += 1
      if guess == letter:
        display[no_of_times -1] = guess
        print("Correct Guess")
    used_letters += guess
    print("Already Guessed Words are " + f"{used_letters}")
    if guess not in chosen_word:
      Lives += 1
      print("Wrong Guess , you lose a life")
    if Lives > 10:
      end_game = True
      print(stages.end_stage)
      print(logo.You_lose)
      print(f"The word was {chosen_word}")
    if blank not in display:
      end_game = True
      print(logo.You_win)
      print(f"The word was {chosen_word}")
  
      
    

        
      


  



