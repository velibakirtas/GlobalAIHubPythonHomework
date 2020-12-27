import time
import random

cScore = 0
pScore = 0   

tour = 3
print(" |Welcome to Rock Paper Scissors game| ".center(100,"~"))
print("""1--Rock\n2--Paper\n3--Scissors""")


while True:
    print("Laps remaining \"{}\"".format(tour))

    cHand = random.randint(1, 3)                
    pHand = int(input("\nWhat is your decision?\n-"))

    if(pHand == 1):
        print("\n{}\t{}\n".format(cHand,pHand))
        if(cHand == 1):     
            print("Draw, score not written\n")
        elif(cHand == 2):   
            cScore += 1
            print("The computer won\nComputer = {}, Player = {}\n".format(cScore,pScore))
            tour -= 1
        elif(cHand == 3):   
            pScore += 1
            print("You won\nComputer = {}, Player = {}\n".format(cScore, pScore))
            tour -= 1

    elif(pHand == 2):
        print("\n{}\t{}\n".format(cHand,pHand))
        if (cHand == 1):   
            pScore += 1
            print("You won\nComputer = {}, Player = {}\n".format(cScore, pScore))
            tour -= 1
        elif (cHand == 2): 
            print("Draw, score not written\n")
        elif (cHand == 3): 
            cScore += 1
            print("The computer won\nComputer = {}, Player = {}\n".format(cScore, pScore))
            tour = tour - 1

    elif (pHand == 3):
        print("\n{}\t{}\n".format(cHand,pHand))
        if (cHand == 1):    
            cScore += 1
            print("The Computer won\nComputer = {}, Player = {}\n".format(cScore, pScore))
            tour -= 1
        elif (cHand == 2):  #Kazanan pHand
            pScore += 1
            print("You won\nComputer = {}, Player = {}\n".format(cScore, pScore))
            tour -= 1
        elif (cHand == 3):  
            print("Draw, score not written\n")

    if(tour == 0):
        print("\nGame over!")
        print("\nResults: Computer = {}, Player = {}\n".format(cScore,pScore))
        time.sleep(5)
        break