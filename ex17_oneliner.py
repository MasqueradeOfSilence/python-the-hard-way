from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
# answer: we could do indata = open(from_file).read(), but then we couldn't do a clean close.
# in_file = open(from_file)
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long\nDoes the output file exist? {exists(to_file)}")

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
#in_file.close()

# open(argv[1], 'w').read().(open(argv[2]).read()).write....
# nope not quite

# NOTE: Converting this to one line may be difficult with imports. What did he mean by this?
# semicolons to separate the lines?
# no, we can do argv directly and just not close the streams, I suppose, and minimize user output
# can we do: __import__('sys').argv ?
# open((__import__('sys').argv)[1], 'w')
# Let's translate line by line actually
# indata will now be open(__import__('sys').argv)[1]).read(), I think
# so nest that within out_file
# outfile is open(all that crap, 'w')
# so now = (open(__import__('sys').argv[1]).read(), 'w')
# then call write on that. 
# but you have to pass indata again
# nope. to_file is just another input! 

# Translate it line by line here: 
# indata = open(__import__('sys').argv[1]).read()

