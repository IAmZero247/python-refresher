from csv import writer, reader

#Ex 1
#default lineteerminator = \r\n
with open('./data/users.csv', 'w') as file:
     csv_writer = writer(file, lineterminator='\n')
     header = ('First Name', 'Last Name', 'Age')
     data = (
         ('Alice', 'S', 22),
         ('Jack', 'S', 23),
         ('JohnP', 28)
     )

     csv_writer.writerow(header)
     csv_writer.writerows(data)

#with open('./data/users.csv') as file:
#    csv_reader = reader(file, delimiter='\t')
#    data = list(csv_reader)
#    for row in data:
#        print(row)
#    for row in data:
#        print(row)

# Ex 2
import csv
fields = ['Name', 'Department', 'Year', 'CGPA']
rows = [['Jai', 'Operator', '2021', '5.0'],
        ['Jen', 'Development', '2021', '5.0'],
        ['Ben', 'Development', '2021', '5.0']]

filename = './data/sample.csv'

with open(filename, 'w') as csvWrite:
    csvObj = csv.writer(csvWrite, lineterminator='\n')
    csvObj.writerow(fields)
    csvObj.writerows(rows)

# Challenge COMPUTE DAILY STOCK RETURN
# daily_return = (todays_price - yesterdays_price) / yesterdays_price
#

import csv
from datetime import datetime
with open('./data/Stock_Data.csv') as f:
    reader = csv.reader(f)
    header = next(reader) #Moved pointer to data 01
    data = [row for row in reader]
    print(header)
    print(data[0])

    #Computation
    type_converted_li_data = []
    for row in data:
        date = datetime.strptime(row[0], "%m/%d/%Y")
        open_price = float(row[1])
        high = float(row[2])
        low = float(row[3])
        close = float(row[4])
        volume = int(row[5])
        adj_close = float(row[6])
        type_converted_li_data.append([date, open_price, high, low, close, volume, adj_close])

print(type_converted_li_data[0])

with open('./data/stock_return.csv', 'w') as w:
    writer = csv.writer(w, lineterminator='\n')
    writer.writerow(["Date", "Return_Price"])

    #Below is a random logic
    for i in range(len(type_converted_li_data) - 1):
            todays_row = type_converted_li_data[i]
            yesterdays_row = type_converted_li_data[i + 1]
            todays_date = todays_row[0]
            todays_price = todays_row[1]
            yesterdays_price = yesterdays_row[-1]
            daily_return = (todays_price - yesterdays_price) / yesterdays_price
            format_date = todays_date.strftime("%m/%d/%y")
            writer.writerow([format_date, daily_return])
