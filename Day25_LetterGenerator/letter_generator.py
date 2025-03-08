# Read the invited names
with open("./Input/Names/invited_names.txt", "r") as invited_names_file:
    names = invited_names_file.readlines()

# Read the starting letter template
with open("./Input/Letters/starting_letter.txt", "r") as starting_letter_file:
    letter_template = starting_letter_file.read()

# Get user input for event customization
event_name = input("Enter the event name: ")
event_date = input("Enter the event date (e.g., March 15, 2025): ")
event_location = input("Enter the event location: ")

# Generate personalized letters
for name in names:
    clean_name = name.strip()
    personalized_letter = letter_template.replace("[name]", clean_name)
    personalized_letter = personalized_letter.replace("[event_name]", event_name)
    personalized_letter = personalized_letter.replace("[event_date]", event_date)
    personalized_letter = personalized_letter.replace("[event_location]", event_location)

    # Save each personalized letter
    with open(f"./Output/ReadyToSend/letter_for_{clean_name}.txt", "w") as output_file:
        output_file.write(personalized_letter)

print("Letters have been successfully created in 'ReadyToSend' folder.")
