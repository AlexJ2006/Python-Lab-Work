#----------------------------------------------------------- BEGIN WORKING WITH NUMpy
#Instructions on sheet 1.3, excercise at the bottom of the sheet.
import numpy as np

#Setting the lists containing the data for modules 1 and 2

#Setting the dictionary to hold the register for the class
student__class_dict_mod1 = {1: "Alex" , 2:"Freya", 3: "Sue", 4: "Steve"}
student_data_mod1 = np.array([]) #And the blank array that will hold the scores 

#Same for Mod2
student_class_dict_mod2 = {1: "Isaac", 2: "Pete", 3: "Lindsay", 4: "Mike"}
student_data_mod2 = ([])

print("")
print("When prompted, please enter the score for each student. ")
print("")

mod1_items = list(student__class_dict_mod1.items())
mod2_items = list(student_class_dict_mod2.items())
i = 0

print("Module 1 Scores")
while i < len(mod1_items): #Setting the loop to iterate over the length of the list.
    key, value = mod1_items[i]
    print("")
    print(value) #Printing the name to the user
    score = int(input("ENTER SCORE: ")) #Getting the score from the user
    student_data_mod1 = np.append(student_data_mod1, score) #Adding the score to the array
    i += 1 # i is incremented by 1
if i == len(mod1_items):
    print("")
    print(student_data_mod1)
    i = 0
    while i <len(mod2_items):
        key, value = mod2_items[i]
        print("")
        print(value)
        score = int(input("ENTER SCORE: "))
        student_data_mod2 = np.append(student_data_mod2, score)
        i += 1
    print("")

#Defining a function to perform min max normalisation
def min_max1(student_data_mod1): #For the first module
    min_val1 = np.min(student_data_mod1)
    max_val1 = np.max(student_data_mod1)
    return(student_data_mod1-min_val1)/(max_val1 - min_val1)

def min_max2(arr): #For the second module
    min_val2 = np.min(arr)
    max_val2 = np.max(arr)
    return(arr-min_val2)/(max_val2 - min_val2)


module1_normalisation = min_max1(student_data_mod1)
module2_normalisation = min_max2(student_data_mod2)

print("")
print("Normalised Values for MODULE 1")
print(module1_normalisation) # Normalised value 1
print("")
print("Normalised Values for MODULE 2")
print(module2_normalisation) # Normalised value 2
print("")

module1_average = np.mean(module1_normalisation) #Finding the average of module 1
print("Module 1 Average: ", module1_average)

module2_average = np.mean(module2_normalisation) #Finding the average of module 2
print("Module 2 Average: ", module2_average)
print("")

if(module1_average > module2_average): # If module one's average is higher...
    print("Module 1 had the higher score, averaging: ", module1_average)
else: # Else, if module two's average is higher
    print("Module 2 had the higher score, averaging", module2_average)
print("")
