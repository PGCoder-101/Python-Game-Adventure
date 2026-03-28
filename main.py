import playgame
import ascii
import functions
import time

role = None
play_again = 'y'

while play_again == 'y':
  playgame.game(role)
  
  play_again = input("Do you want tp play again? Y/N: ").lower().strip()


