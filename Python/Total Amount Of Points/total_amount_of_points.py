"""
CodeWars Challenge #16: Total Number of points
"""

# Solution

"""
Get the total number of points based on the conting 
rule stated in the problem statement

:param (list): games
:return (int): total 
"""
def points(games):
    
    total = 0
	
    for game in games:
        
        scores = game.split(":")
        
        if scores[0] > scores[1]:
            
            total += 3
             
        elif scores[0] == scores[1]:
            
            total += 1
            
    return total