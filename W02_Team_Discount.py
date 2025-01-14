# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Print the day of the week for the user to see.
print(day_of_week)

#vvvvvv
#If the subtotal is $50 or greater and today is Tuesday or Wednesday, 
#your program must subtract 10% from the subtotal

subtotal = float(input("Please enter the subtotal here: "))
if (day_of_week == 1 or day_of_week == 3):
    subtotal = subtotal * 0.9



sales_tax = 0.06 * subtotal
st = round(sales_tax, 2)
total = subtotal + sales_tax
rounded = round(total, 2)
print(f"Sales Tax:{st}")
print(f"Total:{rounded}")













