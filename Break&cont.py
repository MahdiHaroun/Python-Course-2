while True:
    print("this phrase will always print")
    break
    print("Does this phrase print?")

print("We are done with the while loop.") 
#************************************************
x = 0
while x < 10:
    print("we are incrementing x")
    if x % 2 == 0:
        x += 3
        continue
    if x % 3 == 0:
        x += 5
    x += 1
print("Done with our loop! X has the value: " + str(x))


#infinte loop
b = 15

while b < 60:
    b = 5    # resit the value of b to 5 each time the loop runs 
    print("Bugs")
    b = b + 7 