print("=" * 36)
print("    GRADE CALCULATOR")
print("=" * 36)
print()

print("Enter marks for 5 subjects (out of 100 each):")
print("-" * 36)

marks1 = float(input("Enter Subject 1 marks: "))


marks2 = float(input("Enter Subject 2 marks: "))


marks3 = float(input("Enter Subject 3 marks: "))


marks4 = float(input("Enter Subject 4 marks: "))


marks5 = float(input("Enter Subject 5 marks: "))

print("-" * 36)


total = marks1 + marks2 + marks3 + marks4 + marks5


percentage = (total / 500) * 100

print("\n" + "=" * 36)
print("    RESULT")
print("=" * 36)

print(f"Total Marks: {total}/500")
print(f"Percentage: {percentage:.1f}%")

print("-" * 36)


print("GRADE: ", end="")

if percentage >= 90:
    print("A+")
    print("Remark: Outstanding! 🎉")
    
elif percentage >= 85:
    print("A")
    print("Remark: Excellent! ⭐")
    
elif percentage >= 75:
    print("B+")
    print("Remark: Very Good! 👍")
    
elif percentage >= 65:
    print("B")
    print("Remark: Good! 😊")
    
elif percentage >= 55:
    print("C+")
    print("Remark: Above Average! ✔️")
    
elif percentage >= 45:
    print("C")
    print("Remark: Average! 👌")
    
elif percentage >= 35:
    print("D")
    print("Remark: Passed! 😅")
    
else:
    print("F")
    print("Remark: Failed! 😔")

print("=" * 36)


print("\nSTATUS: ", end="")
if percentage >= 35:
    print("PASSED ✅")
else:
    print("FAILED ❌")


print("\nSUBJECT-WISE STATUS:")
print("-" * 25)

print("Subject 1: ", end="")
if marks1 >= 35:
    print("PASS ✅")
else:
    print("FAIL ❌")

print("Subject 2: ", end="")
if marks2 >= 35:
    print("PASS ✅")
else:
    print("FAIL ❌")

print("Subject 3: ", end="")
if marks3 >= 35:
    print("PASS ✅")
else:
    print("FAIL ❌")

print("Subject 4: ", end="")
if marks4 >= 35:
    print("PASS ✅")
else:
    print("FAIL ❌")

print("Subject 5: ", end="")
if marks5 >= 35:
    print("PASS ✅")
else:
    print("FAIL ❌")

print("-" * 36)


print("\nFINAL VERDICT:")
print("-" * 20)

if percentage >= 75:
    print("Congratulations! First Division! 🎊")
    
elif percentage >= 60:
    print("Well done! Second Division! 👍")
    
elif percentage >= 45:
    print("Good! Third Division! ✔️")
    
elif percentage >= 35:
    print("You passed! Work harder next time! 💪")
    
else:
    print("You failed! Better luck next time! 📚")
