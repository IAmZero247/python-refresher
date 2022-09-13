# Link to the Tutorial Video - https://youtu.be/Sul7LtaIKnw

# 1) Creating CSV file
# 2) Adding row
# 3) Adding Multiple Rows
# 4) Reading Rows
# 5) 2nd Approach
#     i) Reading
#     ii) Writing
# 6) Append New Rows at the end of the file
# 7) Updating (update cell, column, row)
# 8) Deleting (column, row, cell)

from csv import writer, reader


#01 Reading CSV File.
path = "./data/Stock_Data.csv"
line = [line for line in open(path)]
print("line 0 ->", line[0])
print("line 1 ->", line[1])
print("type of line1 ->" , type(line[1]))
print("elements header line0 -> ",line[0].strip().split(","))
print("elements line1        -> ",line[1].strip().split(","))

#02 Reading CSV File using open
f = open("./data/Stock_Data.csv")
text = f.read()
f.close()
print(text)
print("type of text -> " , type(text)) # string

#03) With csv:
#1) Python contains a module called csv for handling csv files.
#2) The reader class from the module that is used for reading data from CSV Files.
#3) At first, csv file is opened using open() method by default 'r', the reader() method of CSV module it will create a reader object that iterates throughout the line in csv file.

with open('./data/Stock_Data.csv',  mode = 'r') as file:
    csv_reader = reader(file, delimiter='\t')
#    for row in data:   this will work
#        print(row)
#    for row in data:   iterator on last rows
#        print(row)
    data = list(csv_reader)
    for row in data:
         print(row)


#try:
#    file = open('./data/Stock_Data.csv',  mode = 'r')
#    statements 1
#
#    statements n
#except err:
#    print('Error !')
#finally:
#    file.close()