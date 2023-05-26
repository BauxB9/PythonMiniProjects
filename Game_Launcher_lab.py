
import random

games_won = 0
games_played = 0
while 1:
	print(f"So far, you have wone {games_won}")
	game_choice = int(input("Which game would you like to play \n\t1. Heads or Tails\n\t2.Rock/Paper/Scissors\n\t"))
	if game_choice == 1:
		games_played += 1
			#while 1:
				#try:
					#guess=input("Hello which one do you want to guess Heads or Tails?")
					#break
				#except:
					#print("sorry")
				#except KeyboardInterrupt:
					#print(" ")
					#exit()


			guess=input("Hello which one do you want to guess Heads or Tails?")

			coin_flip = r.randint(1,2)

			if coin_flip == 1 and guess.lower() == "heads":
				print("Correct")
				games_won += 1
			elif coin_flip == 2 and guess.lower() == "tails":
				print("Correct")
				games_won += 1
			else:
				print("Sorry")
	elif game_choice == 2:

			guess = input("Enter rock, paper, scissors: ")

			comp_choice = r.choice(("rock", "paper", "scissors"))

			if guess == comp_choice:
				print("its a draw!")

			elif guess.lower == "rock"
				if comp_choice == "scissors":
					print("You win")
					games_won += 1
				else:
					print("You lose")

			elif guess.lower == "scissors"
				if comp_choice == "paper":
					print("You win")
					games_won += 1
				else:
					print("You lose")

			elif guess.lower == "paper"
				if comp_choice == "rock":
					print("You win")
					games_won += 1
				else:
					print("You lose")

			else:
				print("you must enter one of the three choices")
break

