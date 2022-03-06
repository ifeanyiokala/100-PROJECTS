
NAME = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    type = file.readlines()
with open("./Input/Letters/starting_letter.txt", ) as same:
    home = same.read()
for name in type:
    clean = name.strip()
    new_letter = home.replace(NAME,clean)
    with open(f"./Output/ReadyToSend/ {clean}_letter.txt",mode ="w") as complete_poem :
        complete_poem.write(new_letter)
