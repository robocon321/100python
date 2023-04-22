def add(*a):
    sum = 0
    for i in a:
        sum += i
    return sum

print(add(1, 2, 3))

def model(**kwargs):
    print(kwargs)

class Model:
    def __init__(self, **kwargs):
        self.a = kwargs.get("a")
        self.b = kwargs.get("b")
        self.c = kwargs.get("c")

model = Model(a = 2, b = 3)
print(model.a)
print(model.c)