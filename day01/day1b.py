# Initialize lists
column_a_list = []
column_b_list = []
Count_list = []


file_path = r"C:\Users\ryan_\OneDrive\Documents\coding\python\day1b.csv"

# had to add , encoding='utf-8-sig'
import csv
with open(file_path, mode='r', encoding='utf-8-sig') as file:
    csvFile = csv.reader(file)
    
    for lines in csvFile:
       # print(lines)  # Print the current row
        if len(lines) > 0:  # Ensure the row is not empty
            column_a_list.append(float(lines[0]))  # First column
        if len(lines) > 1:  # Ensure there is a second column
            column_b_list.append(float(lines[1]))  # Second column

column_a_list.sort()
column_b_list.sort()
#print("Column A:", column_a_list)
#print("Column B:", column_b_list)

# This uses a loop I am familiar with
for i in range(len(column_a_list)):
    count = column_b_list.count(column_a_list[i])    
    math = column_a_list[i] * float(count)  
    if math != 0:
        Count_list.append(math)
        print(str(column_a_list[i]) + "," + str(count)+ "," + str(math))
print(Count_list)
print(sum(Count_list))