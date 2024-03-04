# 8. Write a Python program that takes a list of integers as input and returns a 
# new list with only the numbers that are prime.  
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def prime_numbers(input_list):
    return [num for num in input_list if is_prime(num)]

try:
    input_numbers = input("Enter numbers separated by spaces: ")
    input_list = [int(x) for x in input_numbers.split()]
    result = prime_numbers(input_list)
    print("Prime numbers in the list:", result)
except ValueError:
    print("Please enter valid integers separated by spaces.")
except Exception as e:
    print("An error occurred:", e)
#================================OUTPUT=======================
# Enter numbers separated by spaces: 1 3 6 9 16 -9 4 6 8 7 11
# Prime numbers in the list: [3, 7, 11]