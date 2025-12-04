print("Enter two numbers, below:-")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print("You have selected operations such as - Addition, Subtraction, Multiplication, and Dividion only.")

oper = str(input("Enter which operation you want to perform\n"))

if (oper == "Addition"):
  print("Addition of two numbers is:", num1 + num2)

elif (oper == "Subtraction"):
  print("Subtraction of two numbers is:", num1 - num2)

elif (oper == "Multiplication"):
  print("Multiplication of two numbers is:", num1 * num2)

else:
  print("Division of two numbers is:", num1 / num2)
