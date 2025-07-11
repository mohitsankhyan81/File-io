with open("practice1.txt","r") as f:
    data=f.read()

newdata=data.replace("java","python")
print(newdata)