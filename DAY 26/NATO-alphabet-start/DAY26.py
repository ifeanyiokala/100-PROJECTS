#import the pandas library
import pandas as pd

#open the csv file
#convert it to a dictionary 

data = pd.read_csv("NATO-alphabet-start\\nato_phonetic_alphabet.csv")

data_dict = data.set_index("letter")["code"].to_dict()

#Request the user to input a word 
user = input("Enter a word : ").upper()

#Using list comprehension to run it through a loop
space = [data_dict[n] for n in list(user)]

print(space)


        

