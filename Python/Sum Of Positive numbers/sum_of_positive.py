"""
CodeWars Challenge #6: Sum of all positive numbers in an array
"""

# Solution

"""
find the sum of all the positive number in the array
:param (list): number_array
:return (int): sum
"""
def positive_sum(number_array):
   
    sum = 0
    
    for number in number_array:
        
        if number > 0:
            
            sum += number
            
    return sum