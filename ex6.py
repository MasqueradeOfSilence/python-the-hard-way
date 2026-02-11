# This variable tells us how many types of people there are in this excellent joke setup
types_of_people = 10
# And this variable prints that info
x = f"There are {types_of_people} types of people."
# A variable to represent the word binary
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "this is the left side of..."
e = "a string with a right side."

print(w + e)
