"""
CodeWars Challenge #11 : Return a negetive number
"""

# Solution

"""
Convert any number to negative

:param (int): number
:param (int): number (negative)
"""
def make_negative(number):
    
    if number > 0:
        
        number *= -1
    
    return number