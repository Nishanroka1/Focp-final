# Gather user inputs
pizza_count = int(input("How many pizzas ordered? "))
delivery_required = input("Is delivery required? ").lower() == 'y'
is_tuesday = input("Is it Tuesday? ").lower() == 'y'
app_used = input("Did the customer use the app? ").lower() == 'y'

# Define pizza prices and discounts
base_pizza_price = 12
delivery_cost = 2.50
tuesday_discount = 0.50
app_discount = 0.25

# Calculate pizza prices based on discounts
if is_tuesday:
    pizza_price = base_pizza_price * (1 - tuesday_discount)
else:
    pizza_price = base_pizza_price

# Calculate delivery costs based on conditions
if delivery_required:
    if pizza_count >= 5:
        delivery_cost = 0
    else:
        delivery_cost = delivery_cost
else:
    delivery_cost = 0

# Calculate total price
if app_used:
    total_price = pizza_count * pizza_price + delivery_cost
    total_price = total_price * (1 - app_discount)
else:
    total_price = pizza_count * pizza_price + delivery_cost

# Display total price
print("\nTotal Price: £", round(total_price, 2), ".")