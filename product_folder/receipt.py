import csv
import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return:
        A compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row  # Store the whole row as the value

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        exit()  # Exit the program if the file is missing

    return dictionary

def main():
    try:
        # Read the products.csv file into a dictionary
        products_dict = read_dictionary("products.csv", 0)

        # Open the request.csv file for reading
        with open("request.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row

            print("Inkom Emporium\n")

            subtotal = 0
            total_items = 0

            for row in reader:
                product_number, quantity = row
                quantity = int(quantity)
                total_items += quantity

                try:
                    product_info = products_dict[product_number]  # This may raise KeyError
                    product_name = product_info[1]
                    product_price = float(product_info[2])
                    item_total = quantity * product_price
                    subtotal += item_total

                    print(f"{product_name}: {quantity} @ ${product_price:.2f}")

                except KeyError:
                    print("Error: unknown product ID in the request.csv file")
                    print(f"'{product_number}'")
                    exit()  # Exit the program on a KeyError

            # Calculate sales tax and total
            sales_tax = round(subtotal * 0.06, 2)  # Assuming 6% sales tax
            total = round(subtotal + sales_tax, 2)

            # Print totals
            print(f"\nNumber of Items: {total_items}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: ${sales_tax:.2f}")
            print(f"Total: ${total:.2f}")

            print("\nThank you for shopping at the Inkom Emporium.")

            # Print the current date and time
            print(datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"))

            # Survey Invitation
            print("\nWe value your feedback!")
            print("Please take our short online survey at:")
            print("www.inkomemporium.com/survey")

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        exit()  # Exit the program if request.csv is missing

if __name__ == "__main__":
    main()
