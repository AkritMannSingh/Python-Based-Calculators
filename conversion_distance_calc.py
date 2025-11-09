print(
    "In this conversion section we convert the value into - km to miles, km to m, km to cm, and vice versa."
)

print("NOTE:\n")
print("Your value must be in the floating point number.")

value = float(input("Enter the value:"))
unit = str(input("Enter the unit of above number:"))

conv = str(input("Enter the unit that you want to convert the above value:"))

if (conv == "kilometre" and unit == "metre"):
  print("The value in kilometres is:", value / 1000)

elif (conv == "Metre" and unit == "kilometre"):
  print("The value in metres is:", value * 1000)

elif (conv == "kilometre" and unit == "centimetre"):
  print("The value in kilometres is:", value / 100000)

elif (conv == "centimetre" and unit == "kilometre"):
  print("The value in centimetres is:", value * 100000)

elif (conv == "kilometre" and unit == "miles"):
  print("The value in kilometres is :", value * 1.60934)

elif (conv == "miles" and unit == "kilometre"):
  print("The value in miles is:", value / 1.60934)

elif (conv == "metre" and unit == "miles"):
  print("The value in metres is:", value * 1609.34)

elif (conv == "miles" and unit == "metre"):
  print("The value in miles is:", value / 1609.34)

elif (conv == "centimetre" and unit == "miles"):
  print("The value in centimetres is:", value * 160934)

elif (conv == "miles" and unit == "centimetre"):
  print("The value in mile is:", value / 160934)

elif (conv == "centimetre" and unit == "metre"):
  print("The value in metres is:", value * 100)

elif (conv == "metre" and unit == "centimetre"):
  print("The value in centimetres is:", value / 100)

else:
  print(
      "Your value unit and conversion unit both are same.\n Sorry! we cannot convert it."
  )