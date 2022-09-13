from csv import DictReader, DictWriter
from tempfile import NamedTemporaryFile
import shutil

with open('./data/users.csv') as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)

with NamedTemporaryFile(mode='w', delete=False) as temp_file:
    header = ('Name', 'Age')

    csv_writer = DictWriter(
        temp_file,
        fieldnames=header,
        lineterminator='\n'
    )
    csv_writer.writeheader()
    for row in data:
        csv_writer.writerow({
            'Name' : row['First Name'] + " " + row['Last Name'],
            'Age' : row['Age']
        })

    print(temp_file.name)


shutil.move(temp_file.name, './data/users_merged_col.csv')