import os

# ANSI color codes for text formatting
ANSI_COLOR_RESET = "\x1b[0m"
ANSI_COLOR_RED = "\x1b[31m"
ANSI_COLOR_GREEN = "\x1b[32m"
ANSI_COLOR_YELLOW = "\x1b[33m"
ANSI_COLOR_BLUE = "\x1b[34m"
ANSI_COLOR_MAGENTA = "\x1b[35m"
ANSI_COLOR_CYAN = "\x1b[36m"

MAX_ITEMS = 100

class Item:
    def __init__(self, item_number=0, item_name='', price=0.0, stock=0):
        self.item_number = item_number
        self.item_name = item_name
        self.price = price
        self.stock = stock

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text):
    width = 80  # Assuming console width of 80 characters
    length = len(text)
    padding = (width - length) // 2
    print(f"{' ' * padding}{text}{' ' * padding}")

def print_header(text):
    print(f"\n{ANSI_COLOR_CYAN}", end='')
    print_centered(text)
    print(ANSI_COLOR_RESET)

def print_submenu_header(text):
    print(f"\n{ANSI_COLOR_MAGENTA}", end='')
    print_centered(text)
    print(ANSI_COLOR_RESET)

def print_red_text(text):
    print(f"{ANSI_COLOR_RED}{text}{ANSI_COLOR_RESET}")

def print_message(text, color):
    print(f"{color}{text}{ANSI_COLOR_RESET}")

def add_item(inventory, item_count):
    if item_count[0] >= MAX_ITEMS:
        print_red_text("Inventory is full. Cannot add more items.\n")
        return

    item_number = get_valid_integer_input("Enter item number: ")
    item_name = input("Enter item name: ").strip()
    price = get_valid_float_input("Enter price: ")
    stock = get_valid_integer_input("Enter available stock: ")

    new_item = Item(item_number, item_name, price, stock)
    inventory.append(new_item)
    item_count[0] += 1
    print_message("Item added successfully.\n", ANSI_COLOR_GREEN)

def change_item(inventory, item_count):
    item_number = get_valid_integer_input("Enter the item number to change: ")

    for item in inventory:
        if item.item_number == item_number:
            item.item_name = input("Enter new item name: ").strip()
            item.price = get_valid_float_input("Enter new price: ")
            item.stock = get_valid_integer_input("Enter new available stock: ")
            print_message("Item updated successfully.\n", ANSI_COLOR_GREEN)
            return
    
    print_red_text("Item number not found.\n")

def delete_item(inventory, item_count):
    item_number = get_valid_integer_input("Enter the item number to delete: ")

    for i, item in enumerate(inventory):
        if item.item_number == item_number:
            del inventory[i]
            item_count[0] -= 1
            print_message("Item deleted successfully.\n", ANSI_COLOR_GREEN)
            return
    
    print_red_text("Item number not found.\n")

def create_receipt(inventory, item_count):
    receipt = []
    total_amount = 0.0
    total_items = 0

    print("Enter items for the receipt (0 to finish):")

    while True:
        item_number = get_valid_integer_input("Enter item number: ")
        if item_number == 0:
            break

        quantity = get_valid_integer_input("Enter quantity: ")

        for item in inventory:
            if item.item_number == item_number:
                if quantity > item.stock:
                    print_red_text("Quantity exceeds available stock. Try again.\n")
                else:
                    total_item_price = item.price * quantity
                    total_amount += total_item_price
                    item.stock -= quantity
                    total_items += quantity

                    receipt.append({
                        'item_number': item.item_number,
                        'item_name': item.item_name,
                        'price': item.price,
                        'quantity': quantity,
                        'total_item_price': total_item_price
                    })
                break

    print("\nReceipt:")
    print(f"{'Item No':<10} {'Item Name':<20} {'Price':<8} {'Qty':<6} {'Total':<8}")
    for item in receipt:
        print(f"{item['item_number']:<10} {item['item_name']:<20} {item['price']:<8.2f} {item['quantity']:<6} {item['total_item_price']:<8.2f}")

    print(f"\nTotal Items: {total_items}")
    print(f"Total Amount: {total_amount:.2f}")

def display_menu():
    print("Main Menu:")
    print(f"1. {ANSI_COLOR_GREEN}Add a New Item{ANSI_COLOR_RESET}")
    print(f"2. {ANSI_COLOR_YELLOW}Change the Values of an Item{ANSI_COLOR_RESET}")
    print(f"3. {ANSI_COLOR_RED}Delete an Item{ANSI_COLOR_RESET}")
    print(f"4. {ANSI_COLOR_BLUE}Create a Receipt{ANSI_COLOR_RESET}")
    print(f"5. {ANSI_COLOR_MAGENTA}Exit{ANSI_COLOR_RESET}")

def load_inventory(filename, inventory, item_count):
    try:
        with open(filename, 'r') as file:
            while True:
                data = file.read(32)
                if not data:
                    break
                item = Item()
                item.item_number, item.item_name, item.price, item.stock = eval(data)
                inventory.append(item)
                item_count[0] += 1
    except FileNotFoundError:
        print_red_text("Inventory file not found. Creating new inventory with default items.\n")
        add_default_items(inventory, item_count)

def save_inventory(filename, inventory):
    with open(filename, 'w') as file:
        for item in inventory:
            file.write(f"{item.item_number}, '{item.item_name}', {item.price}, {item.stock}\n")

def display_inventory(inventory):
    print("Current Inventory:")
    print(f"{'Item No':<10} {'Item Name':<20} {'Price':<10} {'Stock':<10}")
    for item in inventory:
        print(f"{item.item_number:<10} {item.item_name:<20} {item.price:<10.2f} {item.stock:<10}")

def add_default_items(inventory, item_count):
    default_items = [
        Item(1, "Apple", 0.99, 50),
        Item(2, "Banana", 0.59, 100),
        Item(3, "Orange", 0.79, 80),
        Item(4, "Milk", 1.49, 30),
        Item(5, "Bread", 2.49, 20)
    ]
    for item in default_items:
        inventory.append(item)
        item_count[0] += 1

def get_valid_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print_red_text("Invalid input. Please enter a valid integer.\n")

def get_valid_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print_red_text("Invalid input. Please enter a valid float number.\n")

def main():
    inventory = []
    item_count = [0]

    load_inventory('inventory.txt', inventory, item_count)  # Load initial inventory from file

    if item_count[0] == 0:
        # If no items were loaded, add default items
        add_default_items(inventory, item_count)

    while True:
        clear_screen()
        print_header("Welcome to Small Shop Inventory Management")
        display_inventory(inventory)  # Display inventory before menu
        display_menu()
        choice = get_valid_integer_input("\nEnter your choice: ")

        if choice == 1:
            clear_screen()
            print_submenu_header("Add a New Item")
            add_item(inventory, item_count)
        elif choice == 2:
            clear_screen()
            print_submenu_header("Change the Values of an Item")
            change_item(inventory, item_count[0])
        elif choice == 3:
            clear_screen()
            print_submenu_header("Delete an Item")
            delete_item(inventory, item_count)
        elif choice == 4:
            clear_screen()
            print_submenu_header("Create a Receipt")
            create_receipt(inventory, item_count[0])
        elif choice == 5:
            clear_screen()
            print_header("Exiting the program. Saving inventory...")
            save_inventory('inventory.txt', inventory)  # Save inventory to file before exit
            print("\nInventory saved successfully.\n")
            break
        else:
            clear_screen()
            print_red_text("Invalid choice. Please try again.\n")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
