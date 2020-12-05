from Data import words
from Data import logo
from Data import stages
from Function import game
import replit

def start_function():
  print(logo.hangman_logo)
  print("Do you want to play with computer or friend: ")
  computer_or_friend = input()
  if computer_or_friend.lower() == "computer":
    replit.clear
    game.computer_game()
  elif computer_or_friend.lower() == "friend" :
    print("We are still developing that stage , please come back later")
  else:
    print("Incorrect input , please choose between computer or friend")
    start_function()