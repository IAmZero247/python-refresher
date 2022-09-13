class Person:

    def __init__(self, name):
        self.name = name

    def about_me(self):
        print('about me ,' , self.name )

    @staticmethod
    def echo():
        print('echo echo echo!')

p = Person('alice')
p.about_me()
p.echo()