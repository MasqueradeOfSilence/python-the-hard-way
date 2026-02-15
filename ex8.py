# Declaring a formatter variable
formatter = "{} {} {} {}"

# Print 1 2 3 4
print(formatter.format(1, 2, 3, 4))
# Print the string versions of that
print(formatter.format("one", "two", "three", "four"))
# print four booleans
print(formatter.format(True, False, False, True))
# "I used the formatter to format the formatter" - Thanos
print(formatter.format(formatter, formatter, formatter, formatter))
# Just formats each of these lines with a space in between
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))