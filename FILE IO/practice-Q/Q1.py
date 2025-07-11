# Create a new file practice.txt using Python.
# Add the following data in it:

# # Hi everyone  
# we are learning File I/O  
# using Java.  
# I like programming in Java.


with open("practice.txt","w") as f:
    f.write("Hi Everyone\nWe are learning file I/O\n")
    f.write("Using Java\nI like programing in java\n")
    print(f)