# ============================================
# TASK 3 - Food Ordering System
# Course: Programming for Problem Solving Lab
# Student: Dasari Sai Balaji
# Roll No: 25951A66G0
# Branch: CSM-C
# ============================================

menu = {1: ("Pizza", 200), 2: ("Burger", 120), 3: ("Sandwich", 100)}

def display_menu():
    """Display the food menu."""
    print("\n===== MENU =====")
    for id, (name, price) in menu.items():
        print(f"{id}. {name} - Rs.{price}")
    print("================")

def place_order():
    """Take food order and calculate total bill."""
    total_bill = 0
    n = int(input("How many items to order? "))
    for _ in range(n):
        item_id = int(input("Enter item ID (1-3): "))
        if item_id not in menu:
            print("Invalid item ID!")
            continue
        qty = int(input("Enter quantity: "))
        if qty < 1 or qty > 1000:
            print("Invalid quantity!")
            continue
        name, price = menu[item_id]
        cost = price * qty
        total_bill += cost
        print(f"Added: {name} x{qty} = Rs.{cost}")
    print(f"\nTotal Bill: Rs.{total_bill}")

# Main
display_menu()
place_order()
