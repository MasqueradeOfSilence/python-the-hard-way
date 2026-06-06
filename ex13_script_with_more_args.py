from sys import argv
# Example 13 exercise: Script with more than 3 arguments and good names for each argument
script, first, second, third, fourth = argv
# Note how no space is needed here in the print with comma syntax
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)
