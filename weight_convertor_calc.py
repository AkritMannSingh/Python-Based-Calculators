print("welcome to weight converter\n")

print("we have many weight quantity such as - quintals, kilograms, and grams\n")

print("NOTE:\n")

print("Your value must be floating point number.\n")

print("=========================================================\n")

value = float(input("Enter the value:"))

unit = str(input("Enter the unit of above number:"))

conv = str(input("Enter the Converting Unit:"))

if (conv == "quintals" and unit == "kilograms"):
  print("The value in quintals is:", value / 100)

elif(conv == "kilograms" and unit == "quintals"):
  print("The value in kilograms is:", value * 100)

elif(conv == "quintals" and unit == "grams"):
  print("The value in quintals is:", value / 100000)

elif(conv == "grams" and unit == "quintals"):
  print("The value in grams is:", value * 100000)

elif(conv == "kilograms" and unit == "grams"):
  print("The value in kilograms is:", value / 1000)

elif(conv == "grams" and unit == "kilograms"):
  print("The value in grams is:", value * 1000)

else:
  print("Your value unit and conversion unit both are same.\nSorry! we cannot convert it.")