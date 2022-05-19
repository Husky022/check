a = 200
b = 200
c = 200
d = 200


def func():
    return 100, 200, 300, 400


a, b, c, d = func()

print(a, b, c, d)

my_dict1 = {"found": False}
my_dict2 = {"found": True}

print(my_dict1.get('found'))
print(my_dict2.get('found'))
