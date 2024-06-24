theSum=0 
x=-1 
while (x!=0):
    x=int(input("next number to add up(enter 0 if no more numbers): ")) #input() is a built-in function that reads a line from input, converts it to a string (stripping a trailing newline), and returns that.
    theSum = theSum+x

print(theSum) 

def get_yes_or_no(message):
    valid_input=False
    while not valid_input:
        answer=input(message)
        answer=answer.upper()
        if answer=="Y" or answer=="N":
            valid_input=True
        else:
            print("Please enter Y for yes or N for no.")
    return answer 

response=get_yes_or_no("Do you like lima beans? Enter Y for yes or N for no: ")
if response=="Y":
    print("Great! They are very healthy.")
else:
    print("Too bad. If cooked right, they are quite tasty.")

