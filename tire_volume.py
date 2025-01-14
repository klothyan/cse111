import math

w = float(input("Please enter the width of the tire in mm (ex 205): "))
a = float(input("Please enter the aspect ratio of the tire (ex 60): "))
d = float(input("Please enter the diameter of the wheel in inches (ex 15): "))

v = (math.pi * (w ** 2) * a * (w * a + 2540 * d)) / 10000000000

print(f"The approximate volume is {v:.2f} liters.")