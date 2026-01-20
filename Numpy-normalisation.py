#----------------------------------------------------------- BEGIN WORKING WITH NUMpy
#Instructions on sheet 1.3, excercise at the bottom of the sheet.
import numpy as np

#Setting the lists containing the data for modules 1 and 2
student_data_mod1 = np.array([45, 60, 75, 30, 50])
student_data_mod2 = np.array([78, 82, 90, 65, 85])

#Defining a function to perform min max normalisation
def min_max1(arr): #For the first module
    min_val1 = np.min(arr)
    max_val1 = np.max(arr)
    return(arr-min_val1)/(max_val1 - min_val1)

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
