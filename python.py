def cafe_menu_management(food_items):
    # Greet the customer
    print("Welcome to Desi Dine! We're thrilled to have you with us and look forward to providing you with exceptional service.")
    
    # Display the menu items with prices
    print("\nHere is our menu:")
    for fooditem, price in food_items.items():
        print(f"{fooditem} : RS {price}/-")
    
    order_total = 0
    order_list = []
    
    while True:
        # Prompt the customer to enter their order
        customer_order = input("\nEnter the name of the food item you want to order: ").strip().lower()
        
        # Convert the food items dictionary keys to lowercase
        food_items_lower = {item.lower(): price for item, price in food_items.items()}
        
        # Check if the food item is available
        if customer_order in food_items_lower:
            order_total += food_items_lower[customer_order]
            order_list.append(customer_order.title())  # Store the item with proper case
            print(f"Your food item '{customer_order.title()}' has been added to your order.")
        else:
            print(f"We are sorry, the food item '{customer_order}' is currently unavailable.")
        
        # Ask if they want to add another item
        another_order = input("Do you want to add another food item? (Yes/No): ").strip().lower()
        if another_order != "yes":
            break
    
    # Display the final bill and the items ordered
    if order_list:
        print("\nYou have ordered the following items:")
        for item in order_list:
            print(f"- {item}: RS {food_items[item]}/-")
        print(f"\nThe total bill for your order is: RS {order_total}/-")
    else:
        print("You have not ordered anything.")

# Example menu
food_items = {
    "Butter Chicken": 250,
    "Paneer Butter Masala": 200,
    "Chicken Biryani": 220,
    "Vegetable Biryani": 180,
    "Rogan Josh": 270,
    "Masala Dosa": 80,
    "Idli Sambar": 60,
    "Vada Pav": 30,
    "Pav Bhaji": 100,
    "Chole Bhature": 120,
    "Aloo Paratha": 70,
    "Palak Paneer": 190,
    "Dal Makhani": 150,
    "Samosa": 20,
    "Pani Puri": 40,
    "Chicken Tikka": 200,
    "Mutton Curry": 300,
    "Fish Curry": 220,
    "Prawn Curry": 280,
    "Hyderabadi Biryani": 250,
    "Lamb Biryani": 280,
    "Paneer Tikka": 180,
    "Malai Kofta": 200,
    "Rajma Chawal": 150,
    "Kadhai Paneer": 190,
    "Gulab Jamun": 40,
    "Jalebi": 50,
    "Rasgulla": 40,
    "Lassi": 60,
    "Aloo Gobi": 120,
    "Bhindi Masala": 130,
    "Egg Curry": 140,
    "Mutton Rogan Josh": 320,
    "Tandoori Chicken": 240,
    "Chicken 65": 180,
    "Keema Naan": 100,
    "Garlic Naan": 40,
    "Pulao": 150,
    "Dhokla": 60,
    "Khandvi": 50,
    "Bhel Puri": 40,
    "Sev Puri": 40,
    "Paneer Bhurji": 160,
    "Chicken Seekh Kebab": 200,
    "Mutton Seekh Kebab": 220,
    "Baingan Bharta": 130,
    "Rava Dosa": 90,
    "Medu Vada": 50,
    "Kheer": 70,
    "Rabri": 80
}

# Call the function to take orders
cafe_menu_management(food_items)
