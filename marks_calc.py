print("Write a marks of Subjects.")

total = 0

for i in range(5):
  marks = float(input("Enter marks in subject" + str(i+1) + ":"))
total += marks

perc = total / 5

if perc >= 85:
  grade = 'A'

elif perc >= 75:
  grade = 'B'

elif perc >= 50:
  grade = 'C'

elif perc >= 35:
  grade = 'D'

else:
  grade = "Reappear"

print("Total marks:", total, "\t Percentage:", perc)

print("\t Grade:", grade)