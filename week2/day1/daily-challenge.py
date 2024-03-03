# #imports random for shuffling the string
# import random

# # Ask the user for a string
# user_string = input("Please enter a string with exactly 10 characters: ")

# # Check the length of the string
# if len(user_string) < 10:
#     print("String not long enough")
# elif len(user_string) > 10:
#     print("String too long")
# else:
#     print("Perfect string")
#     # Print the first and last characters of the string
#     print("First character:", user_string[0])
#     print("Last character:", user_string[-1])

#     # Print the string character by character using a for loop
#     print("Building up the string character by character:")
#     built_string = ""
#     for char in user_string:
#         built_string += char
#         print(built_string)

#     char_list = list(user_string)
#     random.shuffle(char_list)
#     jumbled_string = ''.join(char_list)
#     print(f'Jumbled String: {jumbled_string}')