import random

#user = int(input("Heads(0) or Tails(1) and try not to fail: "))
#x = random.randint(0,1)

#if x == user:
	#print("WINNER")

#else:
	#print(f'The answer is {x} and you choose {user}')


user = input("Enter a choice (rock, paper, scissors): ")

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

print(f"\nYou chose {user}, computer chose {computer}.\n")

if user == computer:
    print(f"Both have choose {user}. It's a draw!")

elif user == "rock":
    if computer == "scissors":
        print("You win!")

    else:
        print("You lose!")

elif user == "paper":
    if computer == "rock":
        print("You win!")

    else:
        print("You lose")

elif user == "scissors":
    if computer == "paper":
        print("You win!")

    else:
        print("You lose")