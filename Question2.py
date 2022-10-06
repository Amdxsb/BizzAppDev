"""  Q2. Provide a program to read the CSV file.
 • CSV file has three columns, the first column names, the second column is birthdate(YYYY-MM-DD) the third column is salary.
 • Read the file and display the data and age in the terminal.
 • The file path, delimiter, and quote char are the input by the user.
• The program has to work from the terminal. The input and output have been taken/displayed
on the terminal """


import pandas as pd
import datetime

path = input("Enter the File path \n")
delimit = input("Enter the delimiter \n")
quote = input("Enter the quotechar \n")
Data = pd.read_csv(path,delimiter=delimit,quotechar='"')

print(Data)

print("Calculate the age \n")

Data['BirthDate'] = pd.to_datetime(Data['BirthDate'],dayfirst=True) # converting birthdate(dtype:object) to datetime

def age(dateofbirth): # def function for calculating age
  today = datetime.date.today() # code to see today`s date
  return today.year-dateofbirth.year - ((today.month,today.day)<(dateofbirth.month,dateofbirth.day)) # calculating age

Data['Age'] = Data['BirthDate'].apply(lambda x: age(x)) # calculating age by using lambda function and adding that column in the dataframe

print(Data) # printing the dataframe with a new column - 'age'

