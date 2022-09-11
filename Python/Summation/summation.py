"""
CodeWars Challenge #1: Summation
"""

"""
Calculate the sum of all numbers from a to num
:param (int): num
:return (int): sum
"""
def summation(num):
    
    # sum variable
    sum = 0
    
    for number in range(1, num+1):
        
        sum += number
        
    return sum

if __name__ == "__main__":

    # get the user input
    number = int(input("Enter an integer: "))

    # display the total sum
    print("Total Sum: " + str(summation(number)))
        
    
