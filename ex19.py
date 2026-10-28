# Declaring a function with 2 params.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # printing cheeses
    print(f"You have {cheese_count} cheeses!")
    # printing crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # do I really need to comment this one
    print("Man that's enough for a party!")
    # come on now
    print("Get a blanket.\n")

# informative message to user
print("We can just give the function numbers directly:")
# calling with direct integers
cheese_and_crackers(20, 30)

# informative message
print("OR, we can use variables from our script:")
# variable declaration
amount_of_cheese = 10
# that's actually not enough crackers for me
amount_of_crackers = 50

# we can call the function with variables instead of magic numbers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# i <3 math
print("We can even do math inside too:")
# now we do math with magic numbers and pass that in as params
cheese_and_crackers(10 + 20, 5 + 6)

# you guessed it. informative message to user
print("And we can combine the two, variables and math:")
# no magic numbers, but math!
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
