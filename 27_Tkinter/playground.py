# def add(*args):
#     print(args[0])
#     sum_nums = 0
#     for n in args:
#         sum_nums += n
#     return sum_nums
#
#
# print(add(3, 5, 6, 5, 1))


def calculate(n, **kwargs):
    print(kwargs)
    # for k, v in kwargs.items():
    #     print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car():
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("blue")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.model)