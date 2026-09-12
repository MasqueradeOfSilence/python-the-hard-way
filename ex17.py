from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# answer: we could do indata = open(from_file).read(), but then we couldn't do a clean close.
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")

out_file = open(to_file, 'w')
out_file.write(indata)

print("fin")

out_file.close()
in_file.close()

# Results from running: File is copied successfully!

# Exercises:
# 1. Remove features? okay lol. We will remove the data prompt and some fluff
# 2. I am sure I could make it 1 line long as well. (TODO)