# ####  ===========ABSTRACTION =========used to follow some set of rules================

from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    def area(self):
        pass

class Square(abstract):
    def __init__(self,side):
        self.side=side

class Circle(abstract):
    def __init__(self,radius):
        self.radius=radius

    def perimeter(self):
        pass
    def area(self):
        pass


obj=Circle(5)
        

'''
abstract class rule follow krane k liye hotab h  jo ki abstract class m jo bhi define  method hota h wo usko hr class jisne class crreate class k time abstact pass kia gya h class creatuion k time usko wo rule follow krna hoga
'''