"""
CodeWars Challenge #9: Find Maximum and Minimum Values
in a list
"""

# Solution

"""
Find the minumum number in a list
:param (list): array
:return (int): minimum_number
"""
def minimum(array):
    
    
    minimum_number = array[0]
    
    for number in array:
        
        if number < minimum_number:
            
            minimum_number = number
            
    return minimum_number


"""
Find the Maximum number in a list
:param (list): array
:return (int): maximum_number 
"""
def maximum(array):
    
    
    maximum_number = array[0]
    
    for number in array:
        
        if number > maximum_number:
            
            maximum_number = number
    
    return maximum_number