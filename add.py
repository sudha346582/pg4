# Get input from the user for the first number
num1_str = input("Enter the first number: ")

# Get input from the user for the second number
num2_str = input("Enter the second number: ")

# Convert the input strings to floating-point numbers
# Using float() allows for both integer and decimal inputs
num1 = float(num1_str)
num2 = float(num2_str)

# Perform addition
sum_result = num1 + num2

# Perform Subtraction
difference= num1 - num2

# Display the results
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The product of {num1} and {num2} is: {difference}")