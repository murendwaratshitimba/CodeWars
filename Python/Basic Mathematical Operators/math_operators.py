"""
CodeWars Challenge #10: Mathematical Operators
"""

# Solution

"""
Perform a mathematical operation based on
operation of interest

:param (str): operator
:param (int): value1
:param (int): value2

:return (int): final_value
"""
def basic_op(operator, value1, value2):
    
    final_value = 0
    
    if operator == "+":

        # Addition
        final_value =  value1 + value2
    
    elif operator == "-":
        
        # Substraction
        final_value = value1 - value2
    
    elif operator == "*":
        
        # Multiplication
        final_value =  value1 * value2
    
    else:
        
        # Division
        final_value =  value1 / value2

    return final_value