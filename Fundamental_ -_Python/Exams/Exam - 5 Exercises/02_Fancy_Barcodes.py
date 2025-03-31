import re

number_of_barcodes = int(input())


pattern = re.compile(r"(@#+)(?P<word>[A-Z][a-z0-9A-Z]{4,}[A-Z])(@#+)")
for barcode in range(number_of_barcodes):
    data = input()
    matches = pattern.search(data)
    if not matches:
        print("Invalid barcode")
        continue 
        

    digits_in_string = [char for char in matches['word'] if char.isdigit()]
    print(f"Product group: {''.join(digits_in_string) if digits_in_string else '00'}")

    
    

        







