import math

Items = int(input(f"Please enter the number of items: "))
Items_Box = int(input(f"Please enter the number of items per box: "))

Total = math.ceil (Items / Items_Box)

print(f"When packing {Items} items, packing {Items_Box} items in each box, you will need {Total} boxes.")

