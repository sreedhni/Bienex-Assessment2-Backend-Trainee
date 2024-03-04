from q20 import get_input,get_positive_integer


email = get_input("Enter your email address: ", str, "Invalid email address. Please try again.")
phonenumber = get_input("Enter your number: ", int, "Invalid number. Please enter  valid integer.")
posative_number=get_positive_integer("enter popsative integer: ")

print(f"Email address: {email}")
print(f"Number: {phonenumber}")


#OUTPUT====================================
# Enter your email address: sree
# Enter your number: yyh
# Invalid number. Please enter  valid integer.
# enter popsative integer: -8
# Please enter a positive integer.
# Enter your number: 9048075355
# Email address: sree
# Number: 9048075355

