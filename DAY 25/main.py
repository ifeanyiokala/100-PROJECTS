# with open("./weather_data.csv") as file:
#     temi = file.readlines()
#     print(temi)

# import csv


# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)

# import pandas as pd 

# data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(type(data['temp']))

# data_dict = data.to_dict()
# print(data_dict)


# temp_list = data["temp"].max()
# print(len(temp_list))

# print(data.day)

# print(data[data.temp == temp_list])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# deg = int(monday.temp)*(9/5)+(32) 

# print(f"Temperature is {deg} fahrenhite")

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")

from turtle import color
import pandas as pd 
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

temi =  data["Primary Fur Color"]
Grey = 0 
Red = 0 
Black = 0 
for row in temi :
    if row  ==  "Gray":
        Grey += 1 
    elif row == "Cinnamon":
        Red += 1 
    elif row == "Black":
        Black += 1 
    else:
        continue



data_dict = {
    "Fur_Colors": ["Grey", "Red", "Black"],
    "Value": [Grey,Red,Black]
}

data = pd.DataFrame(data_dict)
data.to_csv("Angela.csv")
