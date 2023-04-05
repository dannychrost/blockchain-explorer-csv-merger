import csv
import sys
from datetime import datetime
# Get the file name from the user
# Open 1 CSV file in write mode
with open(input("Enter the name of the first .csv file to read from: "), "r") as file1, \
    open(input("Enter the name of the second .csv file to read from: "), "r") as file2, \
        open(input("Enter the name of the third .csv file to write to: "), "w") as file3:
    # Create CSV reader and writer objects
    reader1 = csv.reader(file1)
    reader2 = csv.reader(file2)
    file3.truncate(0)
    reader3 = csv.writer(file3)
    # Declare a variable that will tell us the column position of DateTime
    # -1 means we don't know the position yet
    dateTimeColumn = -1
    firstLineR1 = next(reader1)
    firstLineR2 = next(reader2)
    filter = input("Input the column name to filter by: ")
    if filter in firstLineR1 and filter in firstLineR2 \
        and firstLineR1.index(filter) == firstLineR2.index(filter):
        dateTimeColumn = firstLineR1.index(filter)
        print(f'Column position of "{filter}": {dateTimeColumn}')
    else:
        print(f'Column "{filter}" not found in either one or both readable \
              .csv files, or their column positions do not match')
        sys.exit(1)
    endOfFile1 = False
    endOfFile2 = False
    f1MoveOn = True
    f2MoveOn = True
    lineR1 = ""
    lineR2 = ""
    reader3.writerow(firstLineR1)
    i = 0
    while(not endOfFile1 or not endOfFile2):
        if(not endOfFile1 and f1MoveOn):
            try:
                lineR1 = next(reader1)
                f1MoveOn = False
            except StopIteration:
                endOfFile1 = True
                f1MoveOn = False
                print("end of 1")
        if(not endOfFile2 and f2MoveOn):
            try:
                lineR2 = next(reader2)
                f2MoveOn = False
            except StopIteration:
                endOfFile2 = True
                f2MoveOn = False
                print("end of 2")
        # Convert the dates into datetime objects
        date1 = ""
        date2 = ""
        if(not endOfFile1):
            date1 = datetime.strptime(lineR1[dateTimeColumn], "%Y-%m-%d %H:%M:%S")
        if(not endOfFile2):
            date2 = datetime.strptime(lineR2[dateTimeColumn], "%Y-%m-%d %H:%M:%S")
        # Compare the dates
        print(f'endOfFile1: {endOfFile1}')
        print(f'endOfFile2: {endOfFile2}')
        if (not endOfFile1 and endOfFile2):
            reader3.writerow(lineR1)
            f1MoveOn = True
        elif (endOfFile1 and not endOfFile2):
            reader3.writerow(lineR2)
            f2MoveOn = True
            print("howdy")
        elif (endOfFile1 and endOfFile2):
            break
        elif (date1 <= date2):
            reader3.writerow(lineR1)
            f1MoveOn = True
        elif (date1 > date2):
            reader3.writerow(lineR2)
            f2MoveOn = True




    
# ['Txhash', 'Blockno', 'UnixTimestamp', 
# 'DateTime', 'From', 'To', 'ContractAddress', 'Value_IN(ETH)', 
# 'Value_OUT(ETH)', 'CurrentValue @ $1868.21/Eth', 'TxnFee(ETH)', 
# 'TxnFee(USD)', 'Historical $Price/Eth', 'Status', 'ErrCode', 'Method']


    

'''
# Open the .csv files in read mode
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
'''