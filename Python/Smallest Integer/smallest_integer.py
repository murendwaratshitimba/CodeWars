"""
CodeWars Challenge #5: Smallest Number
"""

# Solution

"""
Find the smallest integer in a number array
:param (list): number_array
:return (int): smallest
"""
def find_smallest_int(number_array):
    # Code here
    
    smallest = number_array[0]
    
    for integer in number_array:
        
        if integer < smallest:
            
            smallest = integer
            
    return smallest