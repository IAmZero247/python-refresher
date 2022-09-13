from csv import DictReader, DictWriter
from tempfile import NamedTemporaryFile
import shutil

# Sample Data
#
#First Name,Last Name,Age
#Alice,Sam,22        --> update cell [Alice Johnson 22]
#John,Mark,23        --> remove this whole row
#Wayne,Leon,28
#Marus,Jain,22       --> update row [Jain Marcus 24]
#Neo,Wayne,23
#
#Expected Out
#First Name,Last Name,Age
#Alice,Samuel,22
#Wayne,Leon,28
#Jain,Marcus,24
#Neo,Wayne,23


with open('./data/users.csv') as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)

print(data[0])

#named temp file with disabled autodelete
with NamedTemporaryFile(mode='w', delete=False) as temp_file:
    header = ('First Name', 'Last Name','Age')

    csv_writer = DictWriter(
        temp_file,
        fieldnames=header,
        lineterminator='\n'
    )
    csv_writer.writeheader()
    for row in data:
        if row[header[0]] == 'Alice' and row[header[1]] == 'Sam' :
            csv_writer.writerow({
            'First Name': 'Alice',
            'Last Name': 'Samual',
            'Age': 22
            },)
            continue

        if row[header[0]] == 'John' and row[header[1]] == 'Mark':
            continue
        if row[header[0]] == 'Marus' and row[header[1]] == 'Jain':
            csv_writer.writerow({
                'First Name': 'Jain',
                'Last Name': 'Marcus',
                'Age': 24
            } )
            continue
        csv_writer.writerow(row)

    print(temp_file.name)

shutil.move(temp_file.name, './data/users.csv')
