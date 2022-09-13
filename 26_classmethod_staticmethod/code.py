#
# @classmethod decorator -> first argument is Class Itself
# @staticmethod decorator -> removes ClassLevel/InstanceLevel info from method
# @property decorator -> 1. applies only to method with zero argument
#                        2. method virtually act as property
#                        3. use only when the statments inside method wont change state of
#                           of any of the property inside class
#
#
class ClassTest:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"Called static_method. We don't get any object or class info here.")

    @property
    def property_method(self):
        return self.p1 - self.p2

instance = ClassTest(10 ,5)
#first way - instance
instance.instance_method()
#second way - instance
ClassTest.instance_method(instance)
#class method
ClassTest.class_method()



#static method
ClassTest.static_method()
#property method
print('property decorated method called ', instance.property_method)

