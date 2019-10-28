"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open('foo.txt', 'r')
print(f.read())
''' 'Do you bite your thumb at us, sir?\nI do bite my thumb, sir.\nDo you bite your thumb at us, sir?\nNo, sir. I do not bite my thumb at you, sir, but I bite my thumb, sir.\nDo you quarrel, sir?\nQuarrel, sir? No, sir.' '''
f.close()
#or
with open('foo.txt', 'r') as file:
    read = file.read()
    print(read)
file.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f = open('bar.txt', 'w')
f.write("Is the law on our side, if I say\nay?\nNo.")
f.close()

f = open('bar.txt', 'r')
print(f.read())
f.close()