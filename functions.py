import ascii
import time

DELAY_SECS1 = 1

def start_option(): 
    while True: 
        start = input("Y/N? ").lower().strip()
        print("")
        if start in ['yes', 'y']: 
            print("Alright, you enter the dense jungle, looking back at the pathway.")
            time.sleep(DELAY_SECS1)
            print("You keep on thinking about your decision, but you move on.")
            time.sleep(1)
            print(ascii.forest_ascii())
            print("")
            break

        elif start in ['no', 'n']: 
            print("You hesitate but eventually decide not to risk it.")
            time.sleep(DELAY_SECS1)
            print("You turn back from the dense outskirts of the jungle and travel back along the path.")
            time.sleep(DELAY_SECS1)
            print("Back to your peaceful stroll like nothing was ever discovered.")
            time.sleep(DELAY_SECS1)
            print("")
            exit()

        else:
            print("Please input your option again, as you have entered an invalid option.")
            print("")


def role_option():
    while True: 
        role = input("Do you want to wield knowledge or power? K/P ").lower().strip()

        if role in ['knowledge', 'k']: 
            print(ascii.knowledge_ascii())
            time.sleep(DELAY_SECS1)
            print("Okay, you choose to wield knowledge.")
            time.sleep(DELAY_SECS1)
            print("We'll see how this plays out later for you in the game.")
            time.sleep(DELAY_SECS1)
            print("")
            return 'knowledge'

        elif role in ['power', 'p']: 
            print(ascii.power_ascii())
            time.sleep(DELAY_SECS1)
            print("Hmm... ")
            time.sleep(DELAY_SECS1)
            print("You chose power, interesting.")
            time.sleep(DELAY_SECS1)
            print("")
            return 'power'

        else: 
            print("Sadly, since you have responded incorrectly to his question...")
            time.sleep(DELAY_SECS1)
            print("He slices you in half as he responds in anger.")
            time.sleep(DELAY_SECS1)
            print("Maybe you should have responded correctly to his question...")
            time.sleep(DELAY_SECS1)
            print("Oh well...")
            time.sleep(DELAY_SECS1)
            print(ascii.gameover_ascii())
            print("")
            exit()


def bubbles_obstacle(role):
    while True: 
        option1 = input("Do you want to fight or run? F/R: ").lower().strip()
        print("")

        if option1 == 'f':
            return bubbles_obstacle2(role)

        elif option1 == 'r': 
            print("Whatever it was, it's faster than you.")
            time.sleep(DELAY_SECS1)
            print("Sadly, it catches up to you, and kills you with its acidic bubbles.")
            time.sleep(DELAY_SECS1)
            print(ascii.gameover_ascii())
            exit()

        else:
            print("Invalid choice. Try again.")


def bubbles_obstacle2(role): 
    while True: 

        if role == 'knowledge': 
            print("You can sense where the bubbles are going to come from, as you have chosen the power of knowledge.")

            obstacle1 = input('It is coming to your right! (JUMP, CROUCH, RIGHT, LEFT): ').lower().strip()
            if obstacle1 in ['left', 'l']:
                print("You dodged that one!")
                print("")
            elif obstacle1 in ['jump','j','crouch','c','right','r']:
                print("You incorrectly answered.")
                time.sleep(DELAY_SECS1)
                print("You get hit by the bubble, as acid engulfs you.")
                time.sleep(DELAY_SECS1)
                print("You die.")
                time.sleep(DELAY_SECS1)
                print(ascii.gameover_ascii())
                exit()
            else:
                print("Your indecision has cost you your life.")
                time.sleep(DELAY_SECS1)
                print(ascii.gameover_ascii())
                exit()

            obstacle2 = input('It is coming to your legs! (JUMP, CROUCH, RIGHT, LEFT): ').lower().strip()
            if obstacle2 in ['jump', 'j']:
                print("You dodged that one as well!")
                print("")
            elif obstacle2 in ['crouch','c','right','r','left','l']:
                print("You incorrectly answered.")
                time.sleep(DELAY_SECS1)
                print("You get hit by the bubble, as acid engulfs you.")
                time.sleep(DELAY_SECS1)
                print("You die.")
                time.sleep(DELAY_SECS1)
                print(ascii.gameover_ascii())
                exit()
            else:
                print("Your indecision has cost you your life.")
                time.sleep(DELAY_SECS1)
                print(ascii.gameover_ascii())
                exit()

            obstacle3 = input('It is coming to your left! (JUMP, CROUCH, RIGHT, LEFT): ').lower().strip()
            if obstacle3 in ['right', 'r']:
                print("Phew!")
                print("")
            elif obstacle3 in ['jump','j','crouch','c','left','l']:
                print("You incorrectly answered.")
                time.sleep(DELAY_SECS1)
                print("You get hit by the bubble, as acid engulfs you.")
                time.sleep(DELAY_SECS1)
                print("You die.")
                time.sleep(DELAY_SECS1)
                print(ascii.gameover_ascii())
                exit()
            else:
                print("Your indecision has cost you your life.")
                time.sleep(DELAY_SECS1)
                print(ascii.gameover_ascii())
                exit()

            obstacle4 = input('It is coming to your head! (JUMP, CROUCH, RIGHT, LEFT): ').lower().strip()
            if obstacle4 in ['crouch', 'c']:
                print("You dodged that one!")
                break
            elif obstacle4 in ['left','l','jump','j','right','r']:
                print("You incorrectly answered.")
                time.sleep(DELAY_SECS1)
                print("You get hit by the bubble, as acid engulfs you.")
                time.sleep(DELAY_SECS1)
                print("You die.")
                time.sleep(DELAY_SECS1)
                print(ascii.gameover_ascii())
                exit()
            else:
                print("Your indecision has cost you your life.")
                time.sleep(DELAY_SECS1)
                print(ascii.gameover_ascii())
                exit()

        elif role == 'power': 
            print("Its attacks are meaningless to you.")
            time.sleep(DELAY_SECS1)
            print("You move on to the next stage with ease.")
            break

    return True
