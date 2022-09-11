"""
CodeWars challenge #18: Abbreviate Name
"""

# Solution

"""
Abbreviate name into initials

:param (str): name
:return (str): abbreviated name
"""
def abbrev_name(name):
    
    name_list = name.split(" ")
    
    return name_list[0][0].upper() + "." + name_list[1][0].upper()