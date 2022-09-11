"""
CodeWars Challenge #20: Are you playing Banjo
"""

# Solution

"""
Check if banjo is playing or not
"""
def are_you_playing_banjo(name):
    
    banjo_decision = ""

    if name[0].lower() == "r":
        
        banjo_decision = name + " plays banjo"
    
    else:

        banjo_decision =  name + " does not play banjo"

    return banjo_decision