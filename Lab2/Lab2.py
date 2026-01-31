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

#---------------------------------------------------------------------------------------------------------- #Counting the "Samples per class label" (Drawing a bar chart based on the number of samples)

#import matplotlib.pyplot as plt

#flowers_df['species'].value_counts().plot(kind="bar")

#plt.show()

#---------------------------------------------------------------------------------------------------------- #Creating a box plot using the petal length
#import seaborn as sbn
#import matplotlib.pyplot as plt

#sbn.boxplot(
    #data=flowers_df,
    #y='petal_length',               # vertical boxplot  ; x: horizontal
    #color='skyblue',          # example dark:skyblue
    #linewidth=1,             # edge thickness      
    #fliersize=2,               # size of outlier points
    #flierprops=dict(marker = "o", markerfacecolor= (0.7, 0.2, 0.4), markersize= 5, alpha= 0.7),   # customize outliers
    #medianprops=dict(color='black', linewidth= 2)     # median line
#)

#plt.show()

#---------------------------------------------------------------------------------------------------------- #Using a violin plot 

#import seaborn as sbn
#import matplotlib.pyplot as plt

#sbn.violinplot(
    #data=flowers_df,
    #x='species',       # categorical variable
    #y=5,    # numeric variable
    #palette='Set2',        # multiple colors
    #hue='species',         #splits each species
    #inner='box',
    #linewidth=2,
    #density_norm='width'   # Each violin is scaled to fit the same width, so all categories look equally wide, even if they have different numbers of observations.
#)

#plt.show()

#----------------------------------------------------------------------------------------------------------  #Creating a scatter plot

#import seaborn as sbn
#import matplotlib.pyplot as plt

#sbn.scatterplot(
    #data=flowers_df,    # dataframe name
    #x='petal_length',   # numeric variable on x-axis
    #y='petal_width',    # numeric variable on y-axis
    #hue='species',    # color by class/species
    #style='species',   # different marker style by class
    #palette='Set1'      # color palette
#)

#plt.show()

#---------------------------------------------------------------------------------------------------------- #Creating a Pair Plot

#import seaborn as sbn
#import matplotlib.pyplot as plt

#sbn.pairplot(flowers_df,hue="species")

#plt.show()

#---------------------------------------------------------------------------------------------------------- 
#Detecting and handling missing/null values

#Load the dataset
#Display the column head and data
#Count the number of rows and columns in the dataset

#print(flowers_df.isna()) #Can also use .isnull                                                                              #Detect Missing Values

#print(flowers_df[flowers_df[['sepal_length','sepal_width','petal_length', 'petal_width', 'species']].isna()].any(axis=1))   #Finding columns with missing values

#variable = flowers_df['petal_length'].isna().sum()                                                                           #Count missing values
#print(variable)

flowers_df_updated = pd.read_csv('Iris_missing_values.csv') #Linking to the new CSV file which contains missing data

#flowers_df_updated['species'].dtype        #Obtaining the data type of the column


#----------------------------------------------------------------------------------------------------------                     #MEAN inputation on a single column

flowers_df_updated_2 = flowers_df_updated.copy()

mean_value = flowers_df_updated_2['sepal_length'].mean()
flowers_df_updated_2['sepal_length'].fillna(mean_value)

flowers_df_updated_2['sepal_length'].isna().sum()


