#Course   Week 1: Python Basics   2. Core Elements of Programs (TIME: 54:14)   Exercise: for

"""
Convert the following code into code that uses a for loop.
    
prints 2
prints 4
prints 6
prints 8
prints 10
prints "Goodbye!"

"""

x = 9 #Optional

for x in range(10):
    if x % 2:
        x += 1
        print(x)
print("Goodbye!")
