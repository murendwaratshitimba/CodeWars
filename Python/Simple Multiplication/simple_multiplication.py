"""
CodeWars Challenge #17: Simple Multiplication
"""

# Solution

"""
Perform a simple multiplication based on : 

if the number is even multiply by 8
else muliply by 9

:param (int): number
:return (int): product
"""
def simple_multiplication(number) :
    
    product = number
    
    if number % 2 == 0:
        
        product *= 8
    
    else:
        
        product *= 9

    return product