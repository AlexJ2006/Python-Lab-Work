#Defining the initial List...

students = [["Alice", 82], ["Bob", 92], ["Charlie", 78]]
#print(students)

#-----------------------------------------------------------
#Inserting into the list

#students.append(["David", 88])
#print(students)

#-----------------------------------------------------------
#Insertion using index

#students.insert(1, ["Eve, 90"])
#print(students)

#-----------------------------------------------------------
#Removal

#students.remove(["Charlie", 78])

#-----------------------------------------------------------
#Removal using index

#students.pop(2)
#print(students)

#-----------------------------------------------------------        #Defining the initial list
#Create a dictionary names AI_Students with the details provided

AI_Students = [["Alice", 85], ["Bob", 92], ["Charlie", 78]]
#print(AI_Students)

#-----------------------------------------------------------
#Add a new student to the list

#AI_Students.append(["David", 88])
#print(AI_Students)

#-----------------------------------------------------------
#Update Bob's score as 90

#AI_Students.insert(1, ["Bob", 90])
#AI_Students.remove(["Bob", 92])
#print(AI_Students)

#----------------------------------------------------------- NOT WORKING
#Remove Charlie from the dictionary using del

#del AI_Students[["Charlie", 78]]
#print(AI_Students)

#-----------------------------------------------------------
#Prompt the user with an integer, check the value of the integer and print the messages depending on these rules:
#If the number is negative,  set it to 0 and print.
#If the number is 0, print Zero.
#If the number is 1, print Single.
#If the number is greater than 1, print More.

#number =int(input("Please enter a number: "))

#if number <0:
    #print("0")

#if number == 0:
    #print("Zero")

#if number == 1:
    #print("single")

#if number >1:
    #print("More")

#----------------------------------------------------------- NEED TO FINISH THIS...
#Weather Activity Advisor
#Ask for inputs of temperature (as an int in degrees), rain (as an int 0 if it isn't raining and 1 if it is raining)
#And for wind_speed(integer in km/h)

#Decision rules:

#If it is raining (rain == 1):

#If temperature < 0 → print "Stay inside and drink hot chocolate"

#Else if temperature >= 0 and temperature <= 20 → print "Take an umbrella and go for a walk"

#Else → print "Stay inside and enjoy a book"

#If it is not raining (rain == 0):

#If temperature < 0 → print "Go skiing"

#Else if temperature <= 25 and wind_speed < 15 → print "Go for a run"

#Else if temperature <= 25 and wind_speed >= 15 → print "Fly a kite"

#Else if temperature > 25 → print "Go swimming"

#else:

#display "Invalid input for rain"
#Additional Notes:

#Use only if-elif-else statements (no loops)

#Handle all possible combinations of temperature, rain, and wind_speed

#Print only one activity for the given inputs



#----------------------------------------------------------- BEGIN WORKING WITH NUMpy
#Instructions on sheet 1.3, excercise at the bottom of the sheet.
import numpy as np

#Setting the lists containing the data for modules 1 and 2
student_data_mod1 = np.array([45, 60, 75, 30, 50])
student_data_mod2 = np.array([45, 60, 75, 30, 50])

#Defining a function to perform min max normalisation
def min_max1(arr): #For the first module
    min_val1 = np.min(arr)
    max_val1 = np.max(arr)
    return(arr-min_val1)/(max_val1-min_val1)

def min_max2(arr): #For the second module
    min_val2 = np.min(arr)
    max_val2 = np.max(arr)
    return()

module1_normalisation = min_max1(student_data_mod1)
module2_normalisation = min_max2(student_data_mod2)

print(module1_normalisation)
print(module2_normalisation)
















