def square(x):
    y= x*x
    return y #dont use print , the last print will print a "none 

topSquare = 10
result = square(topSquare)
print("The square of " ,topSquare, " is " ,result)


#**************************************
def weird():
    print("here")
    return 5
    print("there")
    return 10

x = weird()
print(x)     # prints 5 ,first return statement is executed and the function ends
#**************************************
def longer_than_five(list_of_names):
    for name in list_of_names: # iterate over the list to look at each name
        if len(name) > 5: # as soon as you see a name longer than 5 letters,
            return True # then return True!
            # If Python executes that return statement, the function is over and the rest of the code will not run -- you already have your answer!
    return False # You will only get to this line if you
    # iterated over the whole list and did not get a name where
    # the if expression evaluated to True, so at this point, it's correct to return False!

# Here are a couple sample calls to the function with different lists of names. Try running this code in Codelens a few times and make sure you understand exactly what is happening.

list1 = ["Sam","Tera","Sal","Amita"]
list2 = ["Rey","Ayo","Lauren","Natalie"]

print(longer_than_five(list1)) # should print False
print(longer_than_five(list2)) # should print True
#**************************************