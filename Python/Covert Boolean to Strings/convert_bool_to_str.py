"""
CodeWars Challenge #13: Convert a boolean into a string
"""

# Solution

"""
convert a boolen to either "Yes" or "No" strings
:param (bool): boolean
:return (str): condition
"""
def bool_to_word(boolean):
    
    condition = "No"

    if boolean:
        
        condition = "Yes"

    return condition
    
   