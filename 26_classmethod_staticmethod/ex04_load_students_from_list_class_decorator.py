class Student:

    def __init__(self, name , age):
        self.name =name
        self.age = age

    @classmethod
    def get_student_from_dict_as_list(cls, liOfdict):
        li = []
        for row in liOfdict:
            stu=  cls(row['name'] , row['age'])
            li.append(stu)
        return li


dict = [ {
      'name': 'alice',
       'age' : 25
    },
    {
        'name': 'jack',
        'age': 25
    },
    {
        'name': 'john',
        'age': 23
    }
]

print(dict)
li = Student.get_student_from_dict_as_list(dict)
print(len(li))
print(li)
print(li[0].name)
print(li[1].name)
print(li[2].name)