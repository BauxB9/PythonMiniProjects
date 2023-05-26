#Bou Haidara, bouhaidara@uncc.edu
#Lists practice mini-lab




#def n_set():
#Create a new function that will create a list of at least 20 numbers
import random
rand_list = []
lst=20
#Populate that list with random numbers from 0-100
for i in range(lst):
    rand_list.append(random.randint(0,100))
print(rand_list)




#Calculate the average of these numbers, print this output
numAvg = rand_list / [20]
print(numAvg)
# #Remove the highest two numbers from the list, recalculate the average and print
# .sort()
# .remove()
# lst[x::y]
# print(lst)
# #Remove the lowest two numbers from the list, recalculate. Return this value, and print
# .sort()
# .reverse()
# .remove()
# lst[x::y]
# print(lst)






#if __name__ == '__main__':
#main()