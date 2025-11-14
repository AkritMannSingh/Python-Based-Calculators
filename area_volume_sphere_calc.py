import math 
print("Hello! Welcome to Sphere Calculator\n")

r = float(input("Enter the Radius of the sphere:"))

a = math.pi * r * r
v = 4 * math.pi * math.pow(r,3)

print("Radius of the sphere:", r, "metres")

print("Area of the sphere:", a, "units square")

print("Volume of the sphere:", v, "units cube\n")

print("Thank you for using Sphere Calculator!!")

