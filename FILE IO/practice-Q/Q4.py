# WAF to find in which line of the file does the word “learning” occur first.
# Print -1 if the word is not found.
def check_line():
    word="Using"
    data=True
    line_no=1
    with open("practice3.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
        return -1

check_line()
        