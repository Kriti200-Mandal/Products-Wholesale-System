from read import products

def save_data(file_name , header  ):
    f = open(file_name, "w")  #Open the file in write mode to overwrite existing content
    f.write(header)  # write header
    for product in products.values():
        line = ""  # Initialize an empty line to hold the product data
        for i in range(len(product)):
            line += str(product[i]) # Convert each product detail to string and add it to the lin
            if i != len(product) - 1: 
                line += "," # Add a comma between values, except after the last on
        line += "\n" # Add a newline character at the end of the product line
        f.write(line) # Write the constructed line to the file
    f.close()
