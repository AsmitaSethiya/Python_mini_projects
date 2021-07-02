import random

user_wins = 0
Computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    useer_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if useer_input == "q":
        break

    if useer_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if useer_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins +=1
    
    elif useer_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins +=1
    
    elif useer_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins +=1
    
    else:
        print("You lost!")
        Computer_wins += 1            

print("You won", user_wins, "times.")
print("The computer won", Computer_wins, "times")

print("Good by !!!")

