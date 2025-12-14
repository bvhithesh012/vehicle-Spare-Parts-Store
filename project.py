# Vehicle Spare Parts Store

bike_parts = {
    1: ("Engine Oil", 1200),
    2: ("Brake Pads", 850),
    3: ("Chain & Sprocket Kit", 3200),
    4: ("Air Filter", 450),
    5: ("Spark Plug", 300)
}

car_parts = {
    1: ("Car Engine Oil", 1800),
    2: ("Brake Disc", 2500),
    3: ("Clutch Plate", 4200),
    4: ("Oil Filter", 650),
    5: ("Wiper Blades", 900)
}

cart = {}
current_products = {}

while True:
    print("\n--- VEHICLE SPARE PARTS STORE ---")
    print("Select Vehicle Type:")
    print("1. Motorcycle")
    print("2. Car")
    print("3. Exit")

    vehicle_choice = input("Enter choice: ")

    if vehicle_choice == "1":
        current_products = bike_parts
        vehicle_name = "Motorcycle"
    elif vehicle_choice == "2":
        current_products = car_parts
        vehicle_name = "Car"
    elif vehicle_choice == "3":
        print("Thank you for visiting!")
        break
    else:
        print("Invalid choice")
        continue

    while True:
        print(f"\n--- {vehicle_name.upper()} SPARE PARTS STORE ---")
        print("1. View Spare Parts")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Change Vehicle Type")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n--- AVAILABLE SPARE PARTS ---")
            for pid, (name, price) in current_products.items():
                print(f"{pid}. {name} - ₹{price}")

        elif choice == "2":
            pid = int(input("Enter spare part ID: "))
            if pid in current_products:
                qty = int(input("Enter quantity: "))
                name, price = current_products[pid]

                if pid in cart:
                    cart[pid]["qty"] += qty
                else:
                    cart[pid] = {"name": name, "price": price, "qty": qty}

                print("Spare part added to cart.")
            else:
                print("Invalid spare part ID")

        elif choice == "3":
            if not cart:
                print("\nCart is empty.")
            else:
                total = 0
                print("\n--- YOUR CART ---")
                for item in cart.values():
                    subtotal = item["price"] * item["qty"]
                    total += subtotal
                    print(f"{item['name']} x {item['qty']} = ₹{subtotal}")
                print("Total Amount = ₹", total)

        elif choice == "4":
            if not cart:
                print("\nCart is empty. Add items before checkout.")
            else:
                total = 0
                print("\n--- CHECKOUT ---")
                for item in cart.values():
                    total += item["price"] * item["qty"]
                print("Total Payable Amount = ₹", total)
                print("Order placed successfully!")
                cart.clear()

        elif choice == "5":
            print("Changing vehicle type...")
            break

        else:
            print("Invalid choice. Please try again.")
