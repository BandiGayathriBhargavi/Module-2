# Return works like same as in english and any code written after it is ignored.
# 1. Returning a Single Value
def square(number):
    return number * number  
r = square(4)
print(r)
# 2. Returning Multiple Values  
def get_user_data(): #Any number of items can be declared in a function
    name = "Alice"
    age = 30
    return name, age  # Packs into a tuple: ("Alice", 30)
u_n, u_a = get_user_data()  # Unpacking the tuple
print(u_n)  
print(u_a)
# 3. Implicit Returns (None) 
def greet(name):
    print(f"Hello, {name}")  # Missing return statement, so it is implicitly returning None
o = greet("Gayathri Bhargavi") 
print(o)
# 4. Early Exits with Multiple return Statements          
def a_v(num):
    if num >= 0:
        return num     
    else:
        return -num     
r1 = a_v(-7)
print(r1)  
print(a_v(5))    

 

