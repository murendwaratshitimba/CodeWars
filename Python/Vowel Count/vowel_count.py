"""
CodeWars Challenge #3: Vowel Count
"""

# solution

"""
Count how many vowels in a sentence
:param (str): sentence
:return (int): count
"""
def get_count(sentence):
    
    vowels = ["a","e", "i", "o", "u"]
    count = 0
    
    for char in sentence:
        
        if char in vowels:
            
            count += 1
            
    return count