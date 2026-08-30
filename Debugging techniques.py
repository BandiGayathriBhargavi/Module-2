#pdb stands for python debugger. It is a built-in library.pdb = bdb + cmd
#1. Addition of numbers
import pdb
def add(a, b):
    ans = a + b
    return ans
pdb.set_trace()
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
s = add(x, y)
print(s)
#next command is used to execute the next line of code.
#variables currently exist at any pause screen - w (where) 
# ll (long list) to see your current position in the code.
