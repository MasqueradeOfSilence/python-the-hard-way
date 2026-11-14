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

# writing my own function as requested by exercise (3)
def i_eat_all_of_your_cheese_and_crackers_because_i_am_fat(cheese_count_delicious, boxes_of_crackers, gallons_of_gatorade):
    print(f"You had {cheese_count_delicious} cheeses and {boxes_of_crackers} boxes of crackers and {gallons_of_gatorade}"
          f" gallons of Gatorade")
    print("You now have 0 cheeses and 0 crackers, because I ate them all")
    print("better me than your mom, she eats way too many already")
    print(f"I left a tiny bit of gatorade for you tho, there's at least like a sip in there")

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

# exercises: for (1), see comments, for (2), sure Jan
# for (3), fine:
i_eat_all_of_your_cheese_and_crackers_because_i_am_fat(67, 666, 69)
i_eat_all_of_your_cheese_and_crackers_because_i_am_fat(69 - 2, 1924 + 2, 1133 // 4)
cheese_count = 6
bc = 12
gg = 1222
i_eat_all_of_your_cheese_and_crackers_because_i_am_fat(cheese_count, bc, gg)
# that was only 3 ways augh
# 7 more...:
# 1
i_eat_all_of_your_cheese_and_crackers_because_i_am_fat(cheese_count, 69, 420 * 666)

def put_the_value_69_in_because_nice():
    return 69
# 2
i_eat_all_of_your_cheese_and_crackers_because_i_am_fat(put_the_value_69_in_because_nice(), 666, 67)
# 3
i_eat_all_of_your_cheese_and_crackers_because_i_am_fat(cheese_count + 87, put_the_value_69_in_because_nice() - 12, 6)
# 4
your_mom = False
i_eat_all_of_your_cheese_and_crackers_because_i_am_fat(17 if your_mom else 32, 666, 67)
# 5
import random
i_eat_all_of_your_cheese_and_crackers_because_i_am_fat(random.randint(3, 6), random.randint(1924, 55555), 1)
# 6
i_eat_all_of_your_cheese_and_crackers_because_i_am_fat(random.randint(3, 6) if your_mom else 32, gg,
                                                       put_the_value_69_in_because_nice() if random.randint(3, 6) == 4 else 666)
# 7, the last one
i_eat_all_of_your_cheese_and_crackers_because_i_am_fat(int("32"), int("666"), int(your_mom))