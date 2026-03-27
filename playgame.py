import time
import ascii
import functions
from colorama import Style, init, Fore, Back
init(autoreset=True)

DELAY_SECS = 1

def start_game(player_name, role):
    print("Welcome to the:")
    time.sleep(DELAY_SECS)
    print(ascii.title_ascii())
    time.sleep(DELAY_SECS)
    print("You have chosen to embark on a treacherous journey:")
    time.sleep(DELAY_SECS)
    functions.start_option()
    time.sleep(DELAY_SECS)
    print("You keep on inching forward, alert of anything that may pop out.")
    time.sleep(DELAY_SECS)
    print("Suddenly, a goblin pops out, but suprisingly, isn't evil!")
    time.sleep(DELAY_SECS)
    print("He asks: ")
    time.sleep(DELAY_SECS)
    print("")
    role = functions.role_option()
    print("You're surprised at what just occured, and curious as to what may occur.")
    time.sleep(DELAY_SECS)
    print("You suddenly hear popping sounds from behind you.")
    time.sleep(DELAY_SECS)
    print("You turn around, just before bubbles zip past you.")
    time.sleep(DELAY_SECS)
    print(ascii.bubble_ascii())
    time.sleep(DELAY_SECS)
    print(ascii.BUBBLES_ZIP())
    time.sleep(DELAY_SECS)
    print("You just snap out of your reverie, when another one zips past you.")
    time.sleep(DELAY_SECS)
    print("")
    functions.bubbles_obstacle(role)

