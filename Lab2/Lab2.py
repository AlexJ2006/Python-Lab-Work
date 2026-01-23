import pandas as pd #Importing pandas into the program.

flowers_df = pd.read_csv('Lab2/Iris.csv') #Linking to the csv file to use as the dataset.

#---------------------------------------------------------------------------------------------------------- # Displaying the first X number of headers from the dataset.

#print("")
#print(flowers_df.head(10)) #Asking to display the first 10 headers from the csv file. 
#print("") #I chose 10 so that I could see all of the headers.

#---------------------------------------------------------------------------------------------------------- # Finding the number of rows and columns withn the dataset.

#print(flowers_df.shape)

#This returns 150, 5. 150 rows and 5 columns.

#---------------------------------------------------------------------------------------------------------- #Providing a certain number of sample rows from the dataset.

#print("")
#print(flowers_df.sample(20))
#print("")

#---------------------------------------------------------------------------------------------------------- #Viewing the names of columns

#print("")
#print(flowers_df.columns)
#print("")

#----------------------------------------------------------------------------------------------------------  #Slicing (extracting portions of the dataset)

#Trying to print the whole column

#print("")
#print(flowers_df['species'])
#print("")

#----------------------------------------------------------------------------------------------------------  #Slicing and using .unique (returns all distinct values in a series or column)

#print("")
#print(flowers_df['sepal_length'].unique())
#print("")

#---------------------------------------------------------------------------------------------------------- #Basic Statistical Analysis (checking the mean, standard deviation and data distributions)

#Describing (providing a breakdown of the datase)
#For more accurate analysis, you can use any of the following instead of the broader "describe"

#DataFrame.count        -       Count the number of non-NA/null observations.
#DataFrame.max      -       Maximum of the values in the object
#DataFrame.min      -       Minimum of the values in the object
#DataFrame.meanDataFrame.std        -       Mean of the values
#DataFrame.select_dtypes        -       Subset of the DataFrame including/excluding columns based on their type.

#print(flowers_df.describe())       -       Overall View showing each of the above stats

#---------------------------------------------------------------------------------------------------------- #Data Visualisation Tools
#Histogram

#import matplotlib.pyplot as plt
#import seaborn

#Drawing a histogram for the petal length and their count.

#fig, ax = plt.subplots(figsize=(5, 5))

#seaborn.histplot(flowers_df['petal_length'])

#plt.show()

#----------------------------------------------------------------------------------------------------------



