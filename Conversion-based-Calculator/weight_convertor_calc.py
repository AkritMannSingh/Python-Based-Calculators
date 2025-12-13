print("welcome to weight converter\n")
print("we have many weight quantity such as - quintals, kilograms, and grams\n")
print("NOTE:\n")
print("Your value must be floating point number.\n")
print("=========================================================\n")

try:
    value = float(input("Enter the value: "))
    unit = str(input("Enter the unit of above number (quintals/kilograms/grams): ")).lower()
    conv = str(input("Enter the Converting Unit (quintals/kilograms/grams): ")).lower()
    
    print("\n" + "="*50)
    
    if unit == conv:
        print("Your value unit and conversion unit both are same.\nNo conversion needed. Value is:", value, conv)
    
    elif conv == "quintals" and unit == "kilograms":
        result = value / 100
        print(f"The value in quintals is: {result}")
    
    elif conv == "kilograms" and unit == "quintals":
        result = value * 100
        print(f"The value in kilograms is: {result}")
    
    elif conv == "quintals" and unit == "grams":
        result = value / 100000
        print(f"The value in quintals is: {result}")
    
    elif conv == "grams" and unit == "quintals":
        result = value * 100000
        print(f"The value in grams is: {result}")
    
    elif conv == "kilograms" and unit == "grams":
        result = value / 1000
        print(f"The value in kilograms is: {result}")
    
    elif conv == "grams" and unit == "kilograms":
        result = value * 1000
        print(f"The value in grams is: {result}")
    
    else:
        print("Invalid unit combination. Please use only: quintals, kilograms, or grams")
        
except ValueError:
    print("Error: Please enter a valid number for the value!")
except Exception as e:
    print(f"An error occurred: {e}")