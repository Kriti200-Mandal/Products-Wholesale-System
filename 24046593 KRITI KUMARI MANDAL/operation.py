import datetime
from read import products , file_name ,header
from write import save_data



VAT_RATE = 0.13 #13% of VAT


def display_products(file_name ,header):
    print("=" * 80)
    print("ID\t Name\t\t Brand\t\t Qty\t  Price\t Country")
    print("=" * 80)

    code = list(products.keys())
    index = 0

    while index < len(code):
        pid = code[index]
        value = products[pid]
        print(str(pid) + "\t", end="")
        item_index = 0
        while item_index < len(value):
            print(value[item_index] + "\t", end="")
            item_index += 1
        print()
        index += 1
    print("=" * 80)






def purchase(filename, header):
    print(">> Purchase menu selected.")
    try:
        purchased_items = []
        total_qty = 0

        loop = True

        while loop == True:
            product_id = int(input("Enter Product Id to restock: "))
            if product_id in products:
                add_qty = int(input("Enter quantity to add: "))
                if add_qty <= 0:
                    print("Number add to quantity cannot be negative ")
                    continue

                supplier_name = input("Enter supplier name: ")
                cost_price = float(input("Enter your cost price per item: "))
                selling_price = cost_price * 3
                current_qty = int(products[product_id][2])
                updated_qty = current_qty + add_qty

                products[product_id][2] = str(updated_qty)
                products[product_id][3] = str(cost_price)

                item_total = cost_price * add_qty
                vat = item_total * 0.13
                final_price = item_total + vat

                purchased_items.append((product_id, add_qty, item_total, final_price))

                contd = input("Do you want to add more items to the purchase ? (yes/no)!").lower()
                if contd == "no":
                    loop = False
            else:
                print("Invalid product ID. Try again.")
    

        save_data(filename, header)
        time = datetime.datetime.now()
        
        invoice_name = "purchase_invoice_" + str(time.year) + str(time.month) + str(time.day) + str(time.hour) + str(time.minute) + str(time.second) + ".txt"

        file = open(invoice_name, "w")
        file.write("=== PURCHASE INVOICE ===\n")
        file.write("Date: " + str(time) + "\n")
        file.write("Supplier: " + supplier_name + "\n")

        for items in purchased_items:
            pid = items[0]
            file.write("Product: " + products[pid][0] + "\n")
            file.write("Brand: " + products[pid][1] + "\n")
            file.write("Quantity: " + str(items[1]) + "\n")
            file.write("Cost price per item: " + str(products[pid][2]) + "\n")
            file.write("Total cost: Rs " + str(items[2]) + "\n")
            file.write("Total cost including VAT: Rs " + str(items[3]) + "\n")
            file.write("\n")

        file.write("====" * 10)
        file.close()

        print("Purchase completed. Invoice generated.")
        print("\n=== PURCHASE INVOICE ====")
        print("Date: " + str(time) + "\n")
        print("Supplier: " + supplier_name + "\n")

        for items in purchased_items:
            pid = items[0]
            print("Product: " + products[pid][0])
            print("Brand: " + products[pid][1])
            print("Quantity: " + str(items[1]))
            print("Cost price per item: " + str(products[pid][2]))
            print("Total cost: Rs " + str(items[2]))
            print("Total cost including VAT: Rs " + str(items[3]))
            print("====" * 10)

    except:
        print("Invalid input! Please enter correct values.")





#purchase(file_name , header)

VAT_RATE = 0.13 #13% of VAT

def sale(file_name, header):
    print(">> Sale Menu is selected ")
    try:
        customer_name = input("Enter customer name ")
        item_sold = []
        loop = True
        while loop == True:
            product_id = int(input("Enter product id to sell"))
            if product_id in products:
                qty_buy = int(input("Enter quantity to sell"))
                if qty_buy <=0:
                    print(" qunatity should be positive ")
                    continue

                qty_str = ""
                for ch in products[product_id][2]:
                    if ch != '\n':
                        qty_str += ch

                available_qty = int(qty_str)
                free_items = qty_buy // 3
                total_items = qty_buy + free_items

                if available_qty >= total_items:
                    products[product_id][2] = str(available_qty - total_items)
                    cost_price = float(products[product_id][3])
                    selling_price = cost_price * 3
                    total_price = qty_buy * selling_price
                    vat = 0.13 * total_price
                    final_price = total_price + vat
                    item_sold.append((product_id, qty_buy, selling_price, final_price))
                else:
                    print("Not enough stock available.")
            else:
                print("Invalid product ID.")

            contd = input("Do you want to add more items to the purchase ? (yes/no)!").lower()
            if contd == "no":
                loop = False

        save_data(file_name, header)
        time = datetime.datetime.now()
        invoice_name = "sale_invoice_" + str(product_id) + ".txt"
        file = open(invoice_name, "w")
        file.write("=== SALE INVOICE ===\n")
        file.write("Date: " + str(time) + "\n")
        file.write("Customer: " + customer_name + "\n")

        for item in item_sold:
            pid = item[0]
            file.write("Product: " + products[pid][0] + "\n")
            file.write("Brand: " + products[pid][1] + "\n")
            file.write("Quantity: " + str(item[1]) + "\n")
            file.write("Selling Price: " + str(item[2]) + "\n")
            file.write("Total Price (incl. VAT): Rs " + str(item[3]) + "\n")
            file.write("\n")

        file.write("==" * 20)
        file.close()
        print("Sale completed. Invoice generated.")
        
    
        print("\n=== SALE INVOICE ====")
        print("Date: " + str(time) + "\n")
        print("Customer: " + customer_name + "\n")
        for item in item_sold:
           pid = item[0]
            
           print("Product: " + products[pid][0] + "\n")
           print("Quantity: " + str(item[1]) + "\n")
           print("Cost price per item: " + str(cost_price) + "\n")
           print("Total cost: Rs " + str(item[2]) + "\n")
           print("Total cost including VAT "   +str(item[3]) + "\n")
           print("====" * 10)


    except:
        print("Invalid input! Please enter correct values.")


#sale(file_name, header)
