# 7-up Python Game

# user/bot starts counting
# user inputs: n, 7-up

# Bot
# different levels of bot accuracy perhaps
# have an array
# e.g. if accuracy is 80%
# arr = [1, 2, 3, 4, 5]
# random()
# if it chooses 5, bot is wrong
# every other number is "correct"

#Modules
import time

# Variables
comNum = 1
endGame = False
repeat = False

print("Start Game\n")

while endGame == False:
    if comNum % 7 == 0 or str(comNum).__contains__("7"):
        print("\n7-up")
    else:
        print("\n" + str(comNum))
    time.sleep(0.2)
    userNum = input("n: ")
    if (comNum + 1) % 7 == 0  or str(comNum + 1).__contains__("7"):
        if userNum == "7-up":
            print("Correct")
            comNum += 2
        else:
            print("Incorrect - should've said 7-up!")
            print("\nGame End")
            break
    elif (comNum + 1) % 7 != 0:
        if userNum == "7-up":
            print("Incorrect - that number is not a multiple of 7/does not contain a seven!")
            print("\nGame End")
            break
        elif int(userNum) == comNum + 1:
            print("Correct")
            comNum += 2
    else:
        print("Incorrect - wrong number!")
        print("\nGame End")
        endGame = True
        time.sleep(0.5)
        print("\nPlay Again?")
        print(">yes\n>no")
        playAgain = input("")
        if playAgain == "yes":
            repeat = True
            endGame = False
            comNum = 1
        else:
            repeat = False
            endGame = True
            break
