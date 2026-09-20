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

out_file.close()
in_file.close()

# NOTE: Converting this to one line may be difficult with imports. What did he mean by this?
# semicolons to separate the lines?