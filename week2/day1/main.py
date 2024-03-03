# Prompt the user for their first name
first_name = str(input("Please enter your first name: "))

# Prompt the user for their last name
last_name = str(input("Please enter your last name: "))

# Prompt the user for their age
age = int(input(f'Hi {first_name} {last_name}, please enter your age: '))

# Prompt the user for the year they were born
birth_year = int(input("Please enter the year you were born: "))

# Calculate the current year
import datetime
current_year = datetime.datetime.now().year

# Calculate the user's current age
current_age = current_year - birth_year

# Display the user's current age
print("Based on the information provided, you are approximately", current_age, "years old.")