#Author Lemart Bennee

"""
data_utils.py
A helper tool for doing maths and formatting money.
"""

def calc_average(num1, num2, num3, num4, num5):

    """
    This function should calc the average of 5 numbers.
    param:num1: is the first number
    param:num2: is the second number
    param:num3: is the third number
    param:num4: is the fourth number
    param:num5: is the fifth number
    returns: reuturns the average of the 5 numbers
        """
    total = num1 + num2 + num3 + num4 + num5
    average = total / 5
    return average 

def format_currency(amount):
    
    """
    This formats the number to a SOuthAfrican Rand
    param:amount: the number were going to format
    return:str: converts the string to 
    """
    rounded_num = round(amount,2)
    convert_to_string = str(rounded_num)
    rand_value = "R" + convert_to_string
    return rand_value
        
