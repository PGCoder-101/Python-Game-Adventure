import ascii
import time
import random

DELAY_SECS1 = 1.2

def start_option(): 
    while True: 
        start = input("Y/N? ").lower().strip()
        print("")
        if start in ['yes', 'y']: 
            print("You enter the dense jungle, looking back at the pathway.")
            time.sleep(DELAY_SECS1)
            print("You keep on thinking about your decision, but you move on.")
            time.sleep(DELAY_SECS1)
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

        if option1 == 'f' or option1 == 'fight':
            return bubbles_obstacle2(role)

        elif option1 == 'r' or option1 == 'run': 
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
            time.sleep(DELAY_SECS1)
            print("Just move in the opposite direction of the the arrow.")

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

def obstacle_after(role): 
    while True: 
        ask2 = input("Right, Left? ").lower().strip()
        print("")
        if ask2 in ['r', 'right']: 
            print("You walk down that path.")
            time.sleep(DELAY_SECS1)
            print("Slowly, but carefully.")
            time.sleep(DELAY_SECS1)
            print("Until a mysterious creature comes in front of you.")
            time.sleep(DELAY_SECS1)
            print("It is NOT friendly, and kills you.")
            time.sleep(DELAY_SECS1)
            print(ascii.gameover_ascii())
            exit()
        
        elif ask2 in ['l', 'left']: 
            print("You have answered, correctly.")
            time.sleep(DELAY_SECS1)
            print("You traverse down the path, awaiting your next decision/obstacle.")
            print("")
            break
        
        else:
            print("You took too long to answer, the bubble creature was following you and killed you.")
            time.sleep(DELAY_SECS1)
            print("")
            print(ascii.gameover_ascii())
            exit()

def obstacle_after2(role): 
    while True: 
        ask3 = input("Talk/Ignore/Run? ").lower().strip()
        print("")
        if ask3 in ['talk', 't']: 
            print("He is very glad you stopped by and talked to him!")
            time.sleep(DELAY_SECS1)
            print("He tells you a clue for a later obstacle:")
            time.sleep(DELAY_SECS1)
            print("Tun left.")
            time.sleep(DELAY_SECS1)
            break
        elif ask3 in ['ignore', 'i']:
            print("You don't bother the creature, it doesn't bother you.")
            time.sleep(DELAY_SECS1)
            break
        elif ask3 in ['run', 'r']: 
            print("The creature is offended as to your actions.")
            time.sleep(DELAY_SECS1)
            print("It kills you.")
            time.sleep(DELAY_SECS1)
            print(ascii.gameover_ascii())
            exit()
        else: 
            print("You don't decide in time, and the creature thinks you are there to kill him.")
            time.sleep(DELAY_SECS1)
            print("He kills you before you can even say anything.")
            time.sleep(DELAY_SECS1)
            print(ascii.gameover_ascii())
            exit()

def obstacle_after3(role):
    while True:
        print("After narrowly avoiding that encounter, you continue forward to realise the acidic bubble monster has been following you.")
        print("")
        time.sleep(DELAY_SECS1)
        print("Do you run or try to fight again? ")
        print("")
        time.sleep(DELAY_SECS1)
        ask4 = input("Run/Fight? ").lower().strip()
        if role in ['k', 'knowledge'] and ask4 in ['f', 'fight']: 
            print("You now have to answer each riddle it gives you, before it leaves you alone for good.")
            print("")
            riddle1 = input("If an integer is square rooted, the result is 8. What is the integer? ").lower().strip()
            print("")
            if riddle1 in ['64', 'sixty-four', 'sixty four']: 
                print("That was an easy one!")
            else: 
                print("Oh well, bye!")
                time.sleep(DELAY_SECS1)
                print(ascii.gameover_ascii())
                exit()
            
            riddle2 = input("If I am 10 now, and my mother is twice that age, what will be my mother's age in 10 years? ").lower()
            print("")
            if riddle2 in ['30', 'thirty']: 
                print("Hmmm, not bad.")
            else: 
                print("...")
                time.sleep(DELAY_SECS1)
                print(ascii.gameover_ascii())
                exit()

            riddle3 = input("This is the last one. What is the name of the title of this game? ").lower().strip()
            print("")
            if riddle3 in ['jungle adventure', 'ja']: 
                print("Okay. You move on.")
                print("")
                break
            else: 
                print("Seriously?")
                time.sleep(DELAY_SECS1)
                print(ascii.gameover_ascii())
        elif role in ['power', 'p'] and ask4 in ['f','fight']: 
            print("Before the creature can even say anything, you kill it with ease.")
            break
        elif ask4 in ['r', 'run']:
            print("It kills you before you can even react. Wrong choice.")
            time.sleep(DELAY_SECS1)
            print(ascii.gameover_ascii())
            exit()

def infoafterobs3(role):
    print("After finally evading the bubble creature, you continue forward.")
    time.sleep(DELAY_SECS1)
    print("You breathe a sigh of relief as you finally start to get a sense of this place.")
    time.sleep(DELAY_SECS1)
    print("Until, of course. You thought too soon.")
    time.sleep(DELAY_SECS1)
    while True:
        if role in ['p, power']: 
            print("You fall into a hidden pit, but are able to survive it as you have chosen power.")
            time.sleep(DELAY_SECS1)
            break
        elif role in ['k', 'knowledge']: 
            print("You fall into a pit, but survive due to your knowledge on how to make a makeshift crutch.")
            time.sleep(DELAY_SECS1)
            break

def obstacle_after4(): 
    print("Now it's a bit of a luck game.")
    time.sleep(DELAY_SECS1)
    for i in range(3):
        ask21 = int(input("You have to choose a random number between 1 and 5 (inc.) "))
        num = random.randint(1, 5)
        if ask21 == num: 
            print('You are successful and move on to the next stage.')
            time.sleep(DELAY_SECS1)
            break 
        elif ask21 != num: 
            print(f'That is incorrect, however, you have two more chances, the correct number was {num}.')
    else: 
        print("You have guessed incorrectly.")
        time.sleep(DELAY_SECS1)
        print("A trapdoor you promise to yourself not seeing suddenly appears and you fall down and die.")
        time.sleep(DELAY_SECS1)
        print(ascii.gameover_ascii())
        exit()