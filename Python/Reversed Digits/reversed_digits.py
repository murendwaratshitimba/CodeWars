"""
CodeWars Challenge #2: Convert number to reversed array of digits
"""


"""
converts the given integer into a reversed array of digits

:param (int): number
:return (list): reversed_digits
"""
def digitize(number):
    
    reversed_digits = []
    
    for digit in str(number)[-1::-1]:
        
        reversed_digits.append(int(digit))
        
    return reversed_digits
