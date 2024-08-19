<!-- Cafe Menu Management -->
Welcome to the Cafe Menu Management System! This Python script allows customers to interactively browse a menu, place orders, and receive a total bill based on their selections. It's a simple, command-line-based application ideal for a small cafe or restaurant setting.

<!-- Features -->
Display a menu with a variety of food items and their corresponding prices.
Accept customer orders and check for availability.
Handle multiple orders in a single session.
Provide a case-insensitive ordering experience, ensuring that customers can type in any case (uppercase, lowercase, or mixed case).
Calculate and display the total bill after the customer has finished ordering.
How It Works
Menu Display: When the script runs, it greets the customer and displays the full menu with item prices.
Order Placement: The customer is prompted to enter the name of the food item they wish to order. The system checks if the item is available.
Order Confirmation: If the item is available, it is added to the order. If not, a message is displayed indicating that the item is unavailable.
Additional Orders: The customer is asked if they want to add more items to their order. They can continue ordering until they are done.
Total Bill: Once the customer has finished ordering, the script displays a summary of their order and the total amount due.
Usage

<!-- Prerequisites -->

Python 3.x must be installed on your system.
Running the Program
Download or clone this repository to your local machine.

Open a terminal or command prompt.

Navigate to the directory containing the script.

<!-- Run the script using the following command: -->

python cafe_menu_management.py


Follow the on-screen prompts to place your order.

<!-- Example output -->

Welcome to Desi Dine! We're thrilled to have you with us and look forward to providing you with exceptional service.

Here is our menu:
Butter Chicken : RS 250/-
Paneer Butter Masala : RS 200/-
...

Enter the name of the food item you want to order: butter chicken
Your food item 'Butter Chicken' has been added to your order.

Do you want to add another food item? (Yes/No): yes
Enter the name of the food item you want to order: paneer tikka
Your food item 'Paneer Tikka' has been added to your order.

Do you want to add another food item? (Yes/No): no

You have ordered the following items:
- Butter Chicken: RS 250/-
- Paneer Tikka: RS 180/-

The total bill for your order is: RS 430/-

<!-- Code Overview -->
cafe_menu_management(food_items): The main function that handles menu display, order placement, and billing.
food_items: A dictionary containing food items as keys and their prices as values.
Case-Insensitive Input: The function ensures that customer input is case-insensitive by converting all inputs and dictionary keys to lowercase.
Contributing
If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

<!-- License -->
This project is licensed under the MIT License - see the LICENSE file for details.

<!-- Contact -->
If you have any questions or suggestions regarding the project, feel free to reach out.