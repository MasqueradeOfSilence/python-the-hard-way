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
# print("Type the filename again:")
# The < is displayed to the user as well as a place for them to type
# file_again = input("< ")

# Once again, open the file based on what the user input
# txt_again = open(file_again)
# aaaand print out the contents, fascinating!
# print(txt_again.read())

## EXERCISES
# 1, Comments left.
# 2. need to specify "command" after calling open, so the google ai robot doesn't get confused
# 3. ok, command/function/method mean the same thing in this context
# 4. I commented them in lieu of deleting because then I would delete all my carefully crafted comments, and will run it again 
# result: now it doesn't ask for input! wow :O :O :O
# life is full of mysteries and amazing discoveries
# 5. To use only input, we would not depend on argv at all, instead passing the value entered in input to the open() command. 
