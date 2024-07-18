#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

starting_letter_list = []
#TODO-1: Open starting letter and save it into a variable.
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

#TODO-2: Open invited names and save it into a list.
with open("Input/Names/invited_names.txt") as names_file:
    name_list = names_file.readlines()

#TODO-3: Combine starting letter with invited names and save into individual letters.

for n in name_list:
  letter_to_send = letter_contents.replace("[name]", n)
  stripped_name = n.strip()
  file_name = "letter_for_" + stripped_name
  with open(f"./Output/ReadyToSend/{file_name}.txt", mode = "w") as completed_letter:
      completed_letter.write(letter_to_send)


