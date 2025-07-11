# Search if the word “learning” exists in the file or not.

def serch():
    word="Using"
    with  open("practice2.txt","r") as f:
         data=f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")

serch()