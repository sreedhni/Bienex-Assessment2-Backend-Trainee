# 11. Write a Python function called calculate_discounted_price that takes the original price of an item and a discount percentage as input.
# The function should return the discounted price after applying the discount. Ensure that the function handles the case where the discount
# percentage is negative and raises a custom exception called InvalidDiscountError with an appropriate error message. 

class InvalidDiscountError(Exception):
    pass

def calculate_discounted_price(original_price, discount_percentage):
    if discount_percentage < 0:
        raise InvalidDiscountError("Discount percentage cannot be negative")
    if discount_percentage > 100:
        raise InvalidDiscountError("Discount percentage cannot be greater than 100")
    discounted_price = original_price - (original_price * discount_percentage / 100)
    return discounted_price

try:
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    discounted_price = calculate_discounted_price(original_price, discount_percentage)
    print("Discounted price:", discounted_price)
except ValueError:
    print("Please enter valid numbers for original price and discount percentage.")
except InvalidDiscountError as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)

#======================OUTPUT==================================
# Enter the original price: 1000
# Enter the discount percentage: 34
# Discounted price: 660.0
# Enter the original price: 1000
# Enter the discount percentage: -3
# Error: Discount percentage cannot be negative
# Enter the original price: 1000
# Enter the discount percentage: 102
# Error: Discount percentage cannot be greater than 100