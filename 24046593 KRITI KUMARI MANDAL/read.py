

products = {}  # Global dictionary to store product data
file_name = "24046593 KRITI MANDAL.txt"

def load_data(file_name):
    f = open(file_name, "r")
    data = f.readlines()
    f.close()

    header = data[0]   # First line is assumed to be the header (column names)
    index = 1 # Start reading from the second line (index 1)
    product_id = 101 # Start product IDs from 101

    while index < len(data):
        line = data[index].split(",")
        if len(line) < 4: # Skip lines that do not have at least 4 fields
            index += 1
            continue
        try:
            float(line[3])  # Try converting the price to a float to validate it
            cleaned = ""          # Remove newline characters from the price field
            for ch in line[3]:
                if ch != '\n':
                    cleaned += ch 
            line[3] = cleaned # Update the price field without '\n'
            products[product_id] = line
            product_id += 1
        except:
            print("Invalid price on line", index + 1)
        index += 1

    return header
header = load_data(file_name) # Call the function and store the returned header

