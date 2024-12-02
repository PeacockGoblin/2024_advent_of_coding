# Initialize lists
column_a_list = []
column_b_list = []
ABS_list = []
ABS_list_2 = []
Sum_all = 0
file_path = r"C:\Users\ryan_\OneDrive\Documents\coding\python\day1a.csv"

# had to add , encoding='utf-8-sig'
import csv
with open(file_path, mode='r', encoding='utf-8-sig') as file:
    csvFile = csv.reader(file)
    
    for lines in csvFile:
        print(lines)  # Print the current row
        if len(lines) > 0:  # Ensure the row is not empty
            column_a_list.append(float(lines[0]))  # First column
        if len(lines) > 1:  # Ensure there is a second column
            column_b_list.append(float(lines[1]))  # Second column

print("Column A:", column_a_list)
print("Column B:", column_b_list)
print("hello world")

column_a_list.sort()
column_b_list.sort()
print("Column A:", column_a_list)
print("Column B:", column_b_list)

#zip function way I dont really know this that well
ABS_list = [a - b for a, b in zip(column_a_list, column_b_list)]

# This uses a loop I am familiar with
for i in range(len(column_a_list)):
    ABS_list_2.append(abs(column_a_list[i] - column_b_list[i]))

Sum_all = sum(ABS_list_2)
print("ABS_list", ABS_list)    
print("ABS_list", ABS_list_2) 
print(Sum_all)

#I had to look alot up. i have a long way to go
