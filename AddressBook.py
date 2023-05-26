#Bou Haidara, bhaidara@uncc.edu
#https://python-forum.io/thread-18064.html I used this website for structure and understanding how to combine the two a while loop and function


#Write a program that will build a contact list / address book. 
#contactList = {'user' : {'userName' : 'User User', 'userPhone' : 'Number', 'userAddress' : 'Address', 'userAddInfo' : 'Information'}}
contactList = {}
#I tried using a function and with a while loop allows the user to input data when an error has arised
#while 1:
	#try:
		#def contactAdd():
#The user should be asked to enter the name, phone number, and address for each person in the list. 
while 1:
	try:
		#menu = print("\nWelcome to the contact book, please enter the following instructions below")
		userName = input("\n\tWhat is the First and Last Name: ")
		if len(str(userName)) == " ":
			print("\tThank you")
		elif len(str(userName)) == "":
			print("\tPlease enter a valid First and Last name")
		else:
			break
	except:
		print("\n\tPlease enter a valid information")
while 1:
	try:
		userPhone = int(input("\n\tWhat is the Phone Number (numbers only and 10 digits total): "))
		if len(str(userPhone)) != 10:
			print("\tPlease enter 10 total digits only")
		else:
			print("\tThank you")
			break
	except:
		print("\n\tPlease enter a valid digits only")
while 1:
	try:
		userAddress = input("\n\tWhat is the Address: ")
		if userAddress == " ":
			print("\tThank you")
		elif userAddress == "":
			print("\tPlease enter a valid information")
		else:
			break
	except:
		print("\n\tPlease enter a valid information")
while 1:
	try:
		userAddInfo = input("\n\tAdditional information (anything useful): ")
		if userAddInfo == " ":
			print("\tThank you")
		elif userAddInfo == "":
			print("\tPlease enter a valid information")
		else:
			break
	except:
		print("Please enter a valid information")
	#except:
		#pass

#Let the user decide whether or not to enter another set of information or be done. 
#The data should be stored in an appropriately structured dictionary. 
		#def updateBook():
addUser = input("\nWould you like to add contact to Address Book (Y/N): ")
if addUser.lower() == "n":
	add = False
	for i in contactList:
		if i.lower() == userName.lower():
			print("\n\tContact is already in the Address Book")
		elif contactList[i]['userName'].lower() == name.lower():
			print("\n\tYou are going to create a dupilcate")
		else:
			add = True
if addUser.lower() == "y"
	
#There are many forms this dictionary could take,#but think about what would make the most sense for the keys and values.

#When the user decides they are done, print the contents of the dictionary.
		#def contacts():
		
print(contactList)



# contact1 = {name, phoneNum, address, addInfo}
# for name, phone, address, addInfo in contact1.items():
# 	print(phoneNum)
# 	print(userAddress)
# 	print(userAddInfo)
	

#contactlst = (str(name)+" "+str(phone)+" "+str(address)+" "+str(addInfo))



#enumerate(contactlst)

# 		def main():
# 			while True:
# 				Quit = input("If you want to exit out of the Address Book type Y/N: ")
# 				if Quit.lower() == "n":
# 					pass
# 				elif Quit == "y":
# 					break
# 				else:
# 					print("Please enter a valid response")

# if __name__ == '__main__':
# 	main()
# 	quit()