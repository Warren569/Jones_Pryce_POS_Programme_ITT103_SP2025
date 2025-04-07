def initialize_product_catalog():
    return {
        1: {"name": "Flour", "category": "Groceries", "price": 50, "stock": 5},
        2: {"name": "Tablet", "category": "Electronics", "price": 100, "stock": 1},
        3: {"name": "Wireless Headphone", "category": "Electronics", "price": 150, "stock": 4},
        4: {"name": "Eggs", "category": "Groceries", "price": 30, "stock": 30},
        5: {"name": "Mattress", "category": "Household Items", "price": 500, "stock": 9},
        6: {"name": "Watch", "category": "Accessories", "price": 60, "stock": 8},
        7: {"name": "Bottle Water", "category": "Beverages", "price": 10, "stock": 13},
        8: {"name": "Samsung TV", "category": "Electronics", "price": 600, "stock": 10},
        9: {"name": "Rice", "category": "Groceries", "price": 15, "stock": 2},
        10: {"name": "Baby Diapers", "category": "Baby Products", "price": 78, "stock": 2},
    }

def display_products_by_category(product_catalog):
    print("\nProducts by Category:")
    categories = {}
    for product_number, details in product_catalog.items():
        category = details["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(
            f"{product_number}. {details['name']} (Price: ${details['price']}, Stock: {details['stock']})"
        )

    for category, products in categories.items():
        print(f"\nCategory: {category}")
        for product in products:
            print(f"  {product}")

def check_stock(product_catalog, product_number, quantity):
    return product_number in product_catalog and product_catalog[product_number]["stock"] >= quantity

def add_to_cart(cart, product_catalog, product_number, quantity):
    if product_number in product_catalog:
        product = product_catalog[product_number]
        if check_stock(product_catalog, product_number, quantity):
            if product["name"] in cart:
                cart[product["name"]]["quantity"] += quantity
            else:
                cart[product["name"]] = {
                    "category": product["category"],
                    "quantity": quantity,
                    "price": product["price"],
                }
            product["stock"] -= quantity
            print(f"Added {quantity} x {product['name']} to cart.")
        else:
            print(f"Not enough stock for {product['name']}. Only {product['stock']} left.")
    else:
        print("Invalid product number.")

def remove_from_cart(cart, product_name):
    if product_name in cart:
        del cart[product_name]
        print(f"Removed {product_name} from cart.")
    else:
        print("Item not found in cart.")

def view_cart(cart):
    print("\nShopping Cart:")
    for item, details in cart.items():
        print(
            f"{item} ({details['category']}): Quantity={details['quantity']}, "
            f"Unit Price=${details['price']}, Total=${details['quantity'] * details['price']}"
        )

def calculate_totals(cart):
    subtotal = sum(details["quantity"] * details["price"] for details in cart.values())
    discount = subtotal * 0.05 if subtotal > 500 else 0
    tax = (subtotal - discount) * 0.10
    total = subtotal - discount + tax
    return subtotal, discount, tax, total

def process_payment(total):
    print("\nSelect Payment Method:")
    print("1. Cash")
    print("2. Credit/Debit Card")
    print("3. Digital Wallet")
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            return total, float(input("Enter cash amount paid: ")) - total, "Cash"
        elif choice == "2":
            input("Enter card number (16 digits): ")
            return total, 0, "Card"
        elif choice == "3":
            input("Enter digital wallet ID: ")
            return total, 0, "Digital Wallet"
        else:
            print("Invalid choice. Try again.")

def generate_receipt(cart, subtotal, discount, tax, total, amount_paid, change, payment_method):
    print("\n--- Receipt ---")
    print("Best Buy Retail Store")
    print("Purchased Items:")
    for item, details in cart.items():
        print(
            f"{item}: Quantity={details['quantity']}, Unit Price=${details['price']}, "
            f"Total=${details['quantity'] * details['price']}"
        )
    print(
        f"Subtotal: ${subtotal:.2f}\nDiscount: ${discount:.2f}\nSales Tax: ${tax:.2f}\n"
        f"Total Due: ${total:.2f}\nAmount Paid: ${amount_paid:.2f}\nChange: ${change:.2f}\n"
        f"Payment Method: {payment_method}\nThank You!"
    )

def main():
    product_catalog = initialize_product_catalog()
    cart = {}
    while True:
        print("\n--- Best Buy Retail Store ---")
        display_products_by_category(product_catalog)
        print(
            "\n1. Add Item to Cart\n2. Remove Item from Cart\n3. View Cart\n4. Checkout\n5. Exit"
        )
        choice = input("Select an option: ")
        if choice == "1":
            try:
                product_number = int(input("Enter product number: "))
                quantity = int(input("Enter quantity: "))
                add_to_cart(cart, product_catalog, product_number, quantity)
            except ValueError:
                print("Invalid input.")
        elif choice == "2":
            product_name = input("Enter product name to remove: ")
            remove_from_cart(cart, product_name)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            if cart:
                subtotal, discount, tax, total = calculate_totals(cart)
                amount_paid, change, payment_method = process_payment(total)
                generate_receipt(cart, subtotal, discount, tax, total, amount_paid, change, payment_method)
                cart.clear()
            else:
                print("Cart is empty. Add items before checkout.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
