

from read import load_data # Loads product data from the text file into a dictionary
from operation import display_products , sale ,purchase # Imports the product display, sale, and purchase functions


file_name = "24046593 KRITI MANDAL.txt"
header = load_data(file_name)#Load the data and store the header (product dictionary) from the file


display_products(file_name ,header) # Display all available products at the beginning

loop = True # Start the main loop for menu options
while loop:
    print("\n== Main Menu ==")
    print("1. Purchase")
    print("2. Sale")
    print("3. Display Products")
    print("4. Exit")

    try:
        user_choice = int(input("Enter your choice (1-4): ")) 
        if user_choice == 1:
            purchase(file_name, header)# Call purchase function to restock products
        elif user_choice == 2:
            sale(file_name, header)# Call sale function to handle product sales
        elif user_choice == 3:
            display_products(file_name, header) # Call function to display all current products
        elif user_choice == 4:
            print(">> Exiting system. Thank you.")
            loop = False
        else:
            print(">> Invalid option! Please try again.")
    except:
        print("Please enter a valid number.")

