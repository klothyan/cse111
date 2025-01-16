import math

w = float(input("Please enter the width of the tire in mm (ex 205): "))
a = float(input("Please enter the aspect ratio of the tire (ex 60): "))
d = float(input("Please enter the diameter of the wheel in inches (ex 15): "))

v = (math.pi * (w ** 2) * a * (w * a + 2540 * d)) / 10000000000

print(f"The approximate volume is {v:.2f} liters.")

from datetime import datetime
current_date_and_time = datetime.now(tz=None)
print(f"The current date is {current_date_and_time:%Y-%m-%d}.")

with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {w:.2f}, {a:.2f}, {d:.2f}, {v:.2f}", file=volumes_file)

buy = input("Would you like to buy some tires with the dimensions you provided? (Y/N) ")

if buy.lower() == "y":
    print("Thank you! Your tires have been ordered.")
    address = input("Please type your address here so we can deliver them to your house: ")
    print(f"Your address is {address}. Thank you for shopping with us! Have a good day!")

if buy.lower() == "n":
    annoying = input("Are you sure you DON'T want to order this limited time deal? (Y/N)")
    if annoying.lower() == "n":
        print("Thanks for changing your mind! Your tires have been ordered.")
        address = input("Please type your address here so we can deliver them to your house: ")
    print(f"Your address is {address}. Thank you for shopping with us! Have a good day!")

    if annoying.lower() == "y":
        address = input("Please type your address here so we can get to your house: ")
        print(f"Your address is {address}. Have a bad day.")











