
# try:
#     file = open("There was an error")
#     a_dicionary = {"key": "value"}
#     print(a_dicionary["key"])

# except KeyError as error_message:
#     print(f"The Key {error_message} does not exist.")

# else:
#     content = file.read()
#     print(content)    

# finally:
#     raise TypeError("This is an error that I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")
bmi = weight / (height * height)

print(bmi)

