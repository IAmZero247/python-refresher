from pprint import pprint
from csv import DictWriter, DictReader

with open('./data/users2.csv', 'w') as file:
    header = ('First Name', 'Last Name', 'Age')

    csv_writer = DictWriter(
        file,
        fieldnames=header,
        lineterminator='\n'
    )

    data = (
        {
            'First Name': 'Alice',
            'Last Name': 'Sam',
            'Age': 22
        },
        {
            'First Name': 'John',
            'Last Name': 'Mark',
            'Age': 23
        },
        {
            'First Name': 'Wayne',
            'Last Name': 'Leon',
            'Age': 28
        }
    )
    csv_writer.writeheader()

    csv_writer.writerows(data)

with open('./data/users2.csv') as file:
    csv_reader = DictReader(file)
    data = list(csv_reader)
    for row in data:
        print(row)
    for row in data:
        pprint(row)