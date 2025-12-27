cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
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
