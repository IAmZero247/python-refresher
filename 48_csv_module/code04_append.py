
from csv import DictWriter

with open('./data/users2.csv', 'a') as file:

    csv_writer = DictWriter(
        file,
        fieldnames=('First Name', 'Last Name', 'Age'),
        lineterminator='\n'
    )

    data = [
        {
            'First Name': 'Marus',
            'Last Name': 'Jain',
            'Age': 22
        },
        {
            'First Name': 'Neo',
            'Last Name': 'Wayne',
            'Age': 23
        },
    ]

    csv_writer.writerows(data)