#Author Lemart

import random
import datetime
import data_utils

def main ():
    num1 = random.randint(50, 500)
    num2 = random.randint(50, 500)
    num3 = random.randint(50, 500)
    num4 = random.randint(50, 500)
    num5 = random.randint(50, 500)

    todays_date = datetime.date.today()
    average_value = data_utils.calc_average(num1, num2, num3, num4, num5)
    average_currency = data_utils.format_currency(average_value)

    print("Transaction Summary")
    print("Date:", todays_date)
    print("Numbers: ", num1, num2, num3, num4, num5)
    print("Average:", average_currency)

if __name__ == "__main__":
    main()
