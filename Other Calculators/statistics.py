import statistics as stat

print("=" * 36)
print("   QUICK STATS CALCULATOR")
print("=" * 36)

print("\nEnter 4 numbers for analysis:")
n1 = float(input("First number: "))
n2 = float(input("Second number: "))
n3 = float(input("Third number: "))
n4 = float(input("Fourth number: "))

dataset = [n1, n2, n3, n4]

print("\n" + "-" * 36)

mean = stat.mean(dataset)
median = stat.median(dataset)

print(f"📋 Dataset: {dataset}")
print(f"📊 Mean (Average): {mean}")
print(f"🎯 Median: {median}")

print("\n🔍 Manual Mode Detection:")
if n1 == n2 == n3 == n4:
    print("All numbers are the same!")
    print(f"Mode: {n1}")
    
elif (n1 == n2 == n3) or (n1 == n2 == n4) or (n1 == n3 == n4) or (n2 == n3 == n4):
    print("Three numbers are same!")
    if n1 == n2 == n3:
        print(f"Mode: {n1}")
    elif n1 == n2 == n4:
        print(f"Mode: {n1}")
    elif n1 == n3 == n4:
        print(f"Mode: {n1}")
    else:
        print(f"Mode: {n2}")
        
elif n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
    print("Two numbers are same!")
    if n1 == n2:
        print(f"Mode: {n1}")
    elif n1 == n3:
        print(f"Mode: {n1}")
    elif n1 == n4:
        print(f"Mode: {n1}")
    elif n2 == n3:
        print(f"Mode: {n2}")
    elif n2 == n4:
        print(f"Mode: {n2}")
    else:
        print(f"Mode: {n3}")
        
else:
    print("No mode - all numbers are different")


print("\n📈 Data Summary:")
if mean > median:
    print("Mean > Median → Data is RIGHT skewed")
elif mean < median:
    print("Mean < Median → Data is LEFT skewed")
else:
    print("Mean = Median → Data is SYMMETRICAL")

print("\n" + "=" * 36)
print("        ANALYSIS COMPLETE")
print("=" * 36)