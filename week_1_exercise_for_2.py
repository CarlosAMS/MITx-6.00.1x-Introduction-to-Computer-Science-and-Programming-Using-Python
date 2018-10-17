#

"""

Correct! 2. Convert the following code into code that uses a for loop.

prints "Hello!"
prints 10
prints 8
prints 6
prints 4
prints 2

"""


print("Hello!")
for i in range(-10, 0, 2):
    print(-i) #Adding '-' will show the positive output due to we are setting the range starting "-10" to make it work backward.


"""
    Another alternative could be.
    
    
"""

for i in range(x):
    k = i - x
    k + 1
    print(abs(k)) #The 'abs' make the output positive.
