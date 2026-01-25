print("In this conversion section we convert the value into - km to miles, km to m, km to cm, and vice versa.\n")
print("NOTE:")
print("1)Your value must be in the floating point number.\n\n2)You must write in full form (kilometre,metre..)\n")

value = float(input("Enter the value: "))
unit = str(input("\nEnter the unit of above number: \n")).lower()

conv = str(input("\nEnter the unit that you want to convert the above value: \n")).lower()

if conv == "kilometre" and unit == "metre":
    print(f"\nThe value in kilometres is: {value / 1000}")
elif conv == "metre" and unit == "kilometre":
    print(f"\nThe value in metres is: {value * 1000}")
elif conv == "kilometre" and unit == "centimetre":
    print(f"\nThe value in kilometres is: {value / 100000}")
elif conv == "centimetre" and unit == "kilometre":
    print(f"\nThe value in centimetres is: {value * 100000}")
elif conv == "kilometre" and unit == "miles":
    print(f"\nThe value in kilometres is: {value * 1.60934}")
elif conv == "miles" and unit == "kilometre":
    print(f"\nThe value in miles is: {value / 1.60934}")
elif conv == "metre" and unit == "miles":
    print(f"\nThe value in metres is: {value * 1609.34}")
elif conv == "miles" and unit == "metre":
    print(f"\nThe value in miles is: {value / 1609.34}")
elif conv == "centimetre" and unit == "miles":
    print(f"\nThe value in centimetres is: {value * 160934}")
elif conv == "miles" and unit == "centimetre":
    print(f"\nThe value in miles is: {value / 160934}")
elif conv == "metre" and unit == "centimetre":
    print(f"\nThe value in metres is: {value / 100}") 
elif conv == "centimetre" and unit == "metre":
    print(f"\nThe value in centimetres is: {value * 100}") 
else:
    print("\nYour value unit and conversion unit both are same or invalid.\nWe cannot convert it.")