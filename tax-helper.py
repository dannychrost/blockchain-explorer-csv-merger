import csv

# Get the file name from the user

file_name = input("Enter the name of the .csv file: ")

# Open the .csv file in read mode
with open(file_name, 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Declare a variable that will tell us the column position of DateTime
    # -1 means we don't know the position yet
    dateTimeColumn = -1
    # Loop through each row in the .csv file
    for row in reader:
        currentColumn = 0
        # Access each column in the row by index
        # For example, row[0] is the value in the first column
        print(row)
        for column in row:
            if(column == "DateTime"):
                dateTimeColumn =  currentColumn
                currentColumn += 1
            else:
                currentColumn += 1
        print(dateTimeColumn)