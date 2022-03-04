from turtle import home


NAME = "[name]"
# TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Names/invited_names.txt") as file:
    type = file.readlines()
with open("./Input/Letters/starting_letter.txt", ) as same:
    home = same.read()
for name in type:
    clean = name.strip()
    new_letter = home.replace(NAME,clean)
    with open(f"./Output/ReadyToSend/ {clean}_letter.txt",mode ="w") as complete_poem :
        complete_poem.write(new_letter)
