# Lily Trandahl
# UWYO COSC 1010
# 09/25/2024
# Lab 03 
# Lab Section: 15
# Sources, people worked with, help given to: Introducing Lists Lecture Slideshow
# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
states = ["Wyoming", "Colorado", "Montana"]
print(states)
print(states[0])
print(states[-1])
statement = f"{states[1].upper()} is south of {states[0].uppper()}."
print(statement)
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
#print the entire list
#now print the first element in the list
#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
print("Part Two------------------------------------------------------------------------")
states.append("Washington")
states.append("Oregon")
states.append("California")
print(states)
states[-2] = "Maine"
print(states)
states.insert(2, "Texas")
print(states)
del states[3]
print(states)
states.remove("Texas")
print(states)
#Append the following states to your list: Washington, Oregon, California and print your list
#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
#Insert the state Texas to be the third element in the list, again printing your list
#Using the `del` statement remove the fourth item from the list, print your list 
#Remove Texas using its value, print the list
print("Part Three----------------------------------------------------------------------")
print(states)
sorted_states = sorted(states)
print(sorted_states)
states.sort(reverse=True)
print(states)
states.sort(reverse=False)
print(states)
#Temporarily sort your list, print it both sorted and unsorted 
#Permanently sort your list in reverse order, printing it out
#Using the reverse method reverse the list and print it

