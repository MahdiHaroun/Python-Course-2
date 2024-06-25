def func(args): 
    return ret_val
#is equivalent to
func = lambda args: ret_val 
#***************************
def f(x):
    return x - 1

print(f) #<function f at 0x7f8f3c1b7d08>
print(type(f)) #<class 'function'>
print(f(3)) #2

print(lambda x: x-2) #<function <lambda> at 0x7f8f3c1b7d90>
print(type(lambda x: x-2)) #<class 'function'>
print((lambda x: x-2)(6)) #4 


