# This variable tells us how many types of people there are in this excellent joke setup
types_of_people = 10
# And this variable prints that info
x = f"There are {types_of_people} types of people."
# A variable to represent the word binary
binary = "binary"
# And a variable to represent the word don't, because don't
do_not = "don't"
# This cheesy joke is stored in a variable called y
# which probably stands for "you will not laugh"
y = f"Those who know {binary} and those who {do_not}."

# A print statement
print(x)
# Yep. A print statement again.
print(y)

# Using f-strings to print the variable x
print(f"I said: {x}")
# f-strings to print y
print(f"I also said: '{y}'")

# An honest boolean
hilarious = False
# The curly braces are quite Pythonic, used below:
joke_evaluation = "Isn't that joke so funny?! {}"

# Format to display the bool
print(joke_evaluation.format(hilarious))

# A string
w = "This is the left side of..."
# Another string
e = "a string with a right side."

# We concat our strings using the + operator
print(w + e)

# Yeah Zed there are 4 places with a string inside a string.
# There's also a place where an int is placed inside of a string, and another place with a bool.
# But there are only 4 strings inside of strings.
# When you add w and e with a +, this is the concatenation operator. It puts the two strings
#   together, which makes a longer string by definition. It is a purely additive operation.

# your mother # <- BREAK IT: If you uncomment this, it will break the code.
