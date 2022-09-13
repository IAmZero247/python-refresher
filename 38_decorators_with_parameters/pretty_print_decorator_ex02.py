import functools
def pretty_print(symbol):
    def decorator(fun):
        def wrapperfun(text):
            print(symbol*len(text))
            fun(text)
            print(symbol*len(text))
        return wrapperfun
    return  decorator

@pretty_print('#')
def print_name(name):
    print(name)

@pretty_print('$')
def print_city(city):
    print(city)





print_name("alice")
print_city("chennai")