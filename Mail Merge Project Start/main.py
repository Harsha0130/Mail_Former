PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_files:
    names = name_files.readlines()

    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/Letter_to_{stripped_name}", mode="w") as completed_letter:
            completed_letter.write(new_letter)