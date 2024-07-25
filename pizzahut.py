#The prices of the pizza's
pizza_prices = {
    "S": 15,
    "M": 20,
    "L": 25
}

#The pepperoni topping prices
pepperoni_prices = {
    "S": 1,
    "M": 2,
    "L": 2
}

# price for extra cheese
extra_cheese_price = 1

# Function to calculate the final bill
def calculate_final_bill(size, add_pepperoni, extra_cheese):
    # Start with the base price of the pizza
    final_bill = pizza_prices.get(size, 0)
    
    # Add pepperoni price if needed
    if add_pepperoni.lower() == 'yes':
        final_bill += pepperoni_prices.get(size, 0)
    
    # Add extra cheese price if needed
    if extra_cheese.lower() == 'y':
        final_bill += extra_cheese_price
    
    return final_bill

# Function to get valid input
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).upper()
        if user_input in valid_options:
            return user_input
        else:
            print("Option not available. Please try again.")

# Get user input with validation
welcome_message= print("Welcome to Pizza Hut\n")
size = get_valid_input("What kind of Pizza can we get you  (S for Small, M for Medium, L for Large): \n", ["S", "M", "L"])
add_pepperoni = get_valid_input("Want some pepperoni with that? (Yes or No): \n", ["YES", "NO"])
extra_cheese = get_valid_input("How about cheese do you want extra cheese? (Y or N): ", ["Y", "N"])

# Calculate and print the final bill
final_bill = calculate_final_bill(size, add_pepperoni, extra_cheese)
print(f"Your final bill is: ${final_bill}")
