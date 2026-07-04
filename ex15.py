# importing the argv lib
from sys import argv

# parsing script and file name as arguments.
# script is always an arg. The user must provide filename
script, filename = argv

# Opening file based on arg name
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("< ")

txt_again = open(file_again)
print(txt_again.read())
