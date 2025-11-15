import statistics as stat

print("Hey! Welcome to a world of Statistics...\n")

list_input = input("Enter a list of numbers separated by spaces: ")
list1 = [int(x) for x in ulist_input.split()]

list_mean = stat.mean(list1)
list_median = stat.median(list1)
list_mode = stat.mode(list1)

print("Given List:", list1)
print("Mean =", list_mean)
print("Median =", list_median)
print("Mode =", list_mode)

print("=======================================================\n")
print("Thank You for using our Services....")