f=open("name.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()

# 'r'	Important function 
# 'w'	Open for writing, truncates the file first (i.e., overwrites).
# 'x'	Create a new file and open it for writing. Fails if file exists.
# 'a'	Open for writing, appends at the end of the file if it exists.
# 'b'	Open in binary mode.
# 't'	Open in text mode (default).
# '+'	Open for updating (reading and writing).