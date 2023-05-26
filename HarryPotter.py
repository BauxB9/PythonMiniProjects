#Bou Haidara
#bhaidara@uncc.edu

player = int(input("Welcome to Hogwards young wizard.\nWe are going to explore the day in a life of a wizard.\nYou will be using numbers to navigate through the game.\nUse (1) to continue: "))
while 1:
	new_experiment = int(input("\nCheck owl (1) for the latest news on wizards\nBegin a new experiment (2)\n What is your choice: "))
	if new_experiment == 1:
		print ("The prof Harry Potter walked in and saw your not working,\nProf Potter tells you to exit the classroom")
		exit()
	elif new_experiment == 2:
		print("\nExcellent Choice and now its time to make history")
	else:
		print("You entered a incorrect number choice.")
		exit()
	#the first set of choices
	type_experiment = int(input("\nYoung wizard time to choose between \nMagical (1)\nRealistic (2)\npotion experiment: "))
	if type_experiment == 1:
		print("\nYour investigation into Magical experiment will surely benefit all of human kind and revolutionize\nthe way we think about everything!\nYou make it a few steps in your potion making and suddenly the potion started to overflow all over the bench.")
	elif type_experiment == 2:
		print("\nYour investigation into Realistic of experiment will surely benefit all of human kind and revolutionize\nthe way we think about everything!\nYou make it a few steps in your potion making and suddenly the potion started to overflow all over the bench.")
	else:
		print("You entered inccorect number choice")
		exit()
	#indent experiment because of choices
	#exit for wrong choices
	#fix the function because of the number choice


	#chemical_spill = int(input("\nOffff a potion has just spilled and caused a bit of mess.\nWhen you think back to remeber if the potion is\nNon-Hazardous (1)\nVery-Hazardous (2).\nWhich one did you remember to do?: "))
	#if chemical_spill == 1:
		#print("Amazingly no one got hurt")
	#if chemical_spill == 2:
		#print("Oh no, the class is getting filled with toads from the sky.\nSo you conger flying nets to catch them") 

	print("\nYou make it a few steps in to your experiment when you suddenly spill chemicals all over the bench! Was it: ")

	chemical_spill = int(input("\n\t1 (Non-Hazardous)\n\t2 (Very-Hazardous)\nWhich do you choose: "))

	if chemical_spill == 1: #elif is used for ....
			print("Okay great, this isnt a problem")
			chemical_spill = False #False is nonHaz making it to a bool
	elif chemical_spill == 2:
			print("The class is getting filled with water from the ground\nuhh ohh, this requires some quick thinking..")
			chemical_spill = True # making it to a bool
	else: #this allows you to no allow any other input
			print("Invalid input, quitting")
			exit()
	#the second set of choices
	print("Do you...")
	print("\n\t 1. Move down the bench to a different spot and pretend like it never happened")
	print("\n\t 2. Clean up the spill, making sure to abide by proper cleaning protocol.")

	cleanup = input()

	cleanup = (cleanup == 2)
		#hazard = (hazard == "2")
			

	if chemical_spill and cleanup: 
			print("You leave the spill where it is and move forward.  Later that day\nthe postdoc who should have supervising you eats a sandwich where you made the spill.\nOnce he stopped mutating, he really didn’t mind the wings he grew, but the Prof Potter was really\nmad at you anyway.Time to a MAGICIAN :-(")
			exit()
	elif chemical_spill and not cleanup:
			print("Disaster averted! You kept your cool, and aside from some minor chemical burns\n(only on Malfoy jr, of course) everything was fine.")
			
	elif not chemical_spill and cleanup:
			print("This will probably be okay, let’s move on.\nwith only the slight maiming of Malfoy jr.")

	elif not chemical_spill and not cleanup:
			print("You do your due diligence and clean the spill up.  Time to keep going!")
	else:
		print("You have entered inccorect number choice")

	print("You quickly work your way through the rest of the experiment, and to your\nsurprise, the results are amazing! Pride swells in your chest!\nWho would have thought you could have accomplished so much in this potion experiment in just one day")
	#third set of choices

	prize = int(input("Now that you have your amazing results, do you\n1. Rush off to tell your PI?\n2. Attempt to replicate the results before telling your PI?\n3. Screw the PI, you did all the work anyway. Time to write a press release and practice your Nobel acceptance speech!"))

	if prize == 1:
		print("Prof Potter doesn’t appreciate being bothered with unverified results,\nand quickly dismisses you from their office.\nSometime later, the Malfoy jr repeats your experiment and verifies your results,\nbut your initial contribution is largely forgotten.\nIn the end, you get mentioned in the acknowledgments of the paper the potion writes in Science")
	elif prize == 2:
		print("Prof Potter appreciates your diligence and commitment to reproducible science.\nYou go on to publish the work in Nature, and upon graduating you receive numerous offers of prestigious postdoc positions.\nIn your memoirs, you write a touching dedication to the programming instructor who taught you the importance of verifying results.\nCONGRADUALTIONS")
	elif prize == 3:
		print("Prof Potter doesn’t appreciate your attempt at going behind their back,\nbut once media outlets pick up the story of your accomplishments, there’s no stopping you.\nIn a surprise move, Hogwards asks Prof Potter to take a vaction and offers you a tenured position.\nYour experiment leads to numerous other breakthroughs, eventually leading to wizards life expectancy tripling\nand wizards’s first contact with humans life openly.\nA monument is built in dedication to you on New Earth.")
	else:
		print("You entered inccorect number choice")
		break
		exit()
	#final set of choices
