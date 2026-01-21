import numpy as np

#Setting the arrays for module 1 and 2
student_data_mod1 = np.array([])
student_data_mod2 = np.array([])

mod1_data = int(input("Please enter the FIRST score"))

if mod1_data < 0:
    print("ERROR. Please enter a valid score.")

elif mod1_data >=0:
    student_data_mod1.append(mod1_data)
    print("You have added", mod1_data, "to the array")



