import pandas as pd
print (pd.__version__)

#SERIES - A 1 Dimensional array holding data of any type 
#The indexes of the data is noted with Labels.
s = [1,'adsd',5.67] #If you use a dictionary, the keys become the labels
my_s = pd.Series(s, index= ['I', 'II', 'III']) #you can name your labels 
print(my_s)

#DATAFRAME - A multidimentional array/table 
df = { 
    'wednesday': [4.30, 5.00, 6.45],#this is a column 
    'thursday': [12.00, 1.50,3.20]
}
my_df = pd.DataFrame(df, index = ["Maria", "Jacop", "Kimberli"])
print(my_df)

#to locate a row
print(my_df.loc[0]) # the parameter  is the index so it could aslo be "Maria"
#to locate several but specific rows 
#print(df.loc[[0,1]]) loc's parameter is a list of rows

#LOADING/IMPORTING FILES
#to load a csv/sql/etc
pd.read_csv('data.csv')
