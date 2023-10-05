# TODO: Create a letter using starting_letter.txt
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


with open("./Input/Letters/starting_letter.txt", "r") as file:
    letter_content = file.read()

    for name in names:
        striped_name = name.strip()
        modified_name = letter_content.replace("[name]", striped_name)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as mod_letter:
            mod_letter.write(modified_name)
