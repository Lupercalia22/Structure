import abc

class Figure(abc.ABC):
    @abc.abstractmethod
    def square(self):
        pass

class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def square(self):
        return self.r * self.r* 3.14

a = Circle(5)
print(a.square())