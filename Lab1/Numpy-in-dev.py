#----------------------------------------------------------- BEGIN WORKING WITH NUMpy
#Instructions on sheet 1.3, excercise at the bottom of the sheet.
import numpy as np

#Setting the lists containing the data for modules 1 and 2

student_data_mod1 = [[]]
student_data_mod2 = [[]]

print("")
mod1_loop = int(input("Please enter 1 to continue. When you wish to move to module 2, enter M2: "))

while name != "M2":
    print("")
    name = input("ENTER NAME: ")
    print("")
    score = int(input("ENTER SCORE: "))
    student_data_mod1.append([name, score])

if name == "M2":
    print("")
    print("Module 1", student_data_mod1)
    print("")
    mod2_loop = int(input("Please enter your score to get started. When you wish to terminate, enter T: "))
    student_data_mod2.add(mod2_loop)


if mod1_loop == "M2":
    print("")
    mod2_loop = int(input("Please enter your score to get started. When you wish to terminate, enter T "))
    student_data_mod2.add(mod2_loop)

    while mod2_loop >0:
        print("")
        data = int(input("ENTER DATA: "))
        student_data_mod2.add(data)
    
    if data == "T":
        print("Program terminated")

if mod2_loop == "T":
    print("Program terminated")

if mod1_loop == "T":
    print("Program Terminated")

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
print(module1_normalisation) # Normalised value 1
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
