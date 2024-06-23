def square(x):
    y = x * x
    return y

z = square(10)
print(y)     #error , y is not defined in the global scope , it is defined in the local scope of the function square
#**************************************