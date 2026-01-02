# We have 100 cars
cars = 100
# There is a decent amount of space in a car, fitting 4 people,
# because middle seat is for chumps and none of the people here are chumps
space_in_a_car = 4.0
# Number of drivers
drivers = 30
# number of backseat drivers
passengers = 90
# extra cars, sadge
cars_not_driven = cars - drivers
# One driver per car
cars_driven = drivers
# We can fit 4 people in a car and there are 100 cars total, so the capacity is the product of the two
carpool_capacity = cars_driven * space_in_a_car
# simple average computation
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Answering study drill questions:
# car_pool_capacity came up as an error because it hadn't been defined.
# The code had carpool_capacity, not car_pool_capacity.
# 1. If we use 4 instead of 4.0, the mathematics is the same - it just doesn't display the decimal
#   in the equation solution.
# The rest of the study drills for this section are just tips and exercises
