from sys import argv

script, filename = argv

target = open(filename, 'r')

# next: read
# Write a script similar to the last exercise that uses read and argv to read the file you just created.

content = target.read()
print("Fine, here's your file: ")
print(content)

target.close()
