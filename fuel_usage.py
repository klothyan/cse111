def main():
    miles = float(input("Enter the first odometer reading in miles: "))
    miles2 = float(input("Enter the 2nd odometer reading in miles: "))
    fuel_used = float(input("Enter the amount of fuel used in gallons: "))
    mpg = (f"miles_per_gallon({miles}, {miles2}, {fuel_used}")
    lp100k_from_mpg = lp100k
    lp100k = lp100k_from_mpg(mpg)
    print(f"{mpg:.1f} Miles per gallon.")
    print(f"{lp100k:.2f} Liters per 100 kilometers.")

def miles(miles, miles2, fuel_used):
    mpg = abs(miles2 - miles) / fuel_used
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k

main()

















