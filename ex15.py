# importing the argv lib
from sys import argv

# parsing script and file name as arguments.
# script is always an arg. The user must provide filename
script, filename = argv

# Opening file based on arg name
txt = open(filename)

# Tell the user what they just did
print(f"Here's your file {filename}:")
# print out the contents of the text file
print(txt.read())

# Tell the user to type it again, OR ELSE
print("Type the filename again:")
# The < is displayed to the user as well as a place for them to type
file_again = input("< ")

# Once again, open the file based on what the user input
txt_again = open(file_again)
# aaaand print out the contents, fascinating!
print(txt_again.read())

## EXERCISES
# 1, Comments left.
# 2. need to specify "command" after open so the google ai robot doesn't get confused
# 3.
