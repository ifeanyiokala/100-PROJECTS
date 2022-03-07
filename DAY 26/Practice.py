
import random 


# numbers = [1,2,3]
# new_numbers = [n + 1 for n in numbers ]

# print(new_numbers)

# name = "Angela"

# new_list = [n  for n in name]

# print(new_list)


# new_num = [num*2 for num in range(1,5)]

# print(new_num)

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]


# short_names = [name.upper() for name in names if len(name) > 6]

# print(short_names)

# names = []


# student_scores = {student:random.randint(1,100) for student in names }

# passed_students = {key:value for (key,value)  in student_scores.items() if value >= 70}

# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# sentence_1 = sentence.split()


student_dict = {"student": ["Angela", "James", "Lily"],
                "score":[56, 76, 98] 
}
# for (key,value) in student_dict.items():
#     print(key)

import pandas 

student_data_frame = pandas.DataFrame(student_dict)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)





# space = []
# for n in sentence_1:
#   hope = n.len()
#   space.append(hope)
  
# print(space)

