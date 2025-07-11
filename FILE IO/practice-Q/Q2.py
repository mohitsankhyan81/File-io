# WAF that replaces all occurrences of “java” with “python” in the above file.

with open("practice1.txt","r") as f:
    data=f.read()

newdata=data.replace("java","python")
print(newdata)