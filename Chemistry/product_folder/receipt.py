import csv

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row  # Store the whole row as the value
    
    return dictionary

def main():
    # Read the products.csv file into a dictionary
    products_dict = read_dictionary("products.csv", 0)
    print("Products Dictionary:")
    print(products_dict)
    print()
    
    # Open the request.csv file for reading
    with open("request.csv", mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        # Process each row in request.csv
        print("Requested Items:")
        for row in reader:
            product_number, quantity = row
            quantity = int(quantity)
            
            if product_number in products_dict:
                product_info = products_dict[product_number]
                product_name = product_info[1]
                product_price = float(product_info[2])
                print(f"{product_name}: {quantity} @ ${product_price:.2f}")
            else:
                print(f"Product {product_number} not found.")
    
if __name__ == "__main__":
    main()
