# IMPERATIVE APPROCH  

a=11
b=1
print(a+b)


# FUNCTIONAL APPROCH

def add(a,b):
    print(a+b)

add(23,34)



# OOPS
#  function inside class is METHOD aand  variiable declare inside class is ATTRIBUTE
class Factory:
    x=12   #attribute
    def greet(self):   #method
        print("good day sir")

    print("hello")

print(Factory().x)
Factory().greet()

# -------------------------------------------------------
# objects

obj=Factory()  # object created
print(obj.x)
obj.greet()

# -------------------------------------------------

# CONSTRUCTOR   --> iski jarurat tb pdti h jb hm log ko function ko jaise parameter dete  h to  isme hm log class m parameter nhi de skte to isiliiye constructor ka use hota h , jo ki program run honte hi innitiate ho jayta h apne aap
 


class Factory2:
    def __init__(self,material,zips,pocket):   # __xyx__  ye type ko dunder method bolte h
        self.material=material 
        self.zips=zips
        self.pocket=pocket
    def show(self):
        print(f"your products details are {self.material},{self.pocket},{self.zips}")

reebok=Factory2("leather",3,2)
campus=Factory2("nylon",4,3)

print(reebok.pocket)
print(campus.pocket)
# yha pr --self-- ka kaam ye h ki wo variable reebok ki locatin ko target krega aur parameterko referance dega jaise ki reebok.material ...etc

reebok.show()

# ------------------------------------------------------------------------------

#  ATTRIBUTES_..> class , instance
#  method types--> instance, class ,static method

class Animal:
    name="lion"   #class attribute

    def __init__(self,age):
        self.age=age  # instance attribute
     
    def show(self): # instance method
        pass

#  CLASS M SIRF INSTANCE METHOD HI BNTE H KYUKI  JB BHI KOI FUNCTION DECLARE KRTE H CLASS M TO USME SELF PASS KRNE SE INSTANCE CREATE HO JATA H 

#  self targets the  object location/instace

    @classmethod      #decorator
    def hello(cls):
        print("how are you?")


# here cls targets the class location

# static method dont access class nor objects

    @staticmethod
    def static():
        print("how are u")

obj=Animal(12)

obj.hello()



# ======================================================================================================


# INHERITANCE

class FactoryMumbai:   # parent class/superclass
    a= "hell from inside factory"

    def hello(self):
        print("hello instance method")

class FactoryPune(FactoryMumbai):  # child class / subclass

    pass


obj=FactoryPune()
obj2=FactoryPune()

obj2.hello()


# ### EXAMPLE 2
# .single inheritance 
class Animal:
    def __init__(self,name):
        self.name= name

    def show(self):
        print(f"name is {self.name}")
    
   # 
class Human(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age

    def show(self):
        print(f"name is {self.name},{self.age}")

a1=Animal("lion")
h1=Human("ayush",22)

h1.show()
a1.show()

# # method over riding ---> ye class k function ko method bolte h,       yha show method dono k liye same h pr done ka alag use h    
# 
# 
# 
#
#  multiple inheritance
# class Robots(Animal,Human):
#     name3="charlie3"

# rob=Robots("xcv")
# rob.show()


# -----------------
# multilevel inheritance

class Mumbai:
    def __init__(self,material,zips):
        self.material=material
        self.zips=zips

    def show(self):
        print(f"{self.material},{self.zips}")

class Pune(Mumbai):
    def __init__(self,material,zips,color):
        super.__init__(material,zips)
        self.color=color


class UP(Pune):
    def __init__(self,material,zips,color,pockets):
        super.__init__(material,zips,color)
        self.pockets=pockets


# bag=UP()


# ============
# hierchical inheritaance---> same multilevel jais e h pr iska mtlb hota h  kki jb ek class multiple class inherit hui h 


# -----------------------POLYMORPHISM---------------------------------------------------------------------
# tyype 1 polymorphismmm
#  METHOD OVER RIDING ---> JB HMRE PASS 2 CLASS HO AUR EK DUSRE CLASS KO INHERIT KIA HO TB AGAR DONO CLASS M SAME METHOD DEFINE HUA HO TB CHILD CLASS KA METHOD PARENT CLASS K METHD KO OVER RIDE KR DETA H 


class pen:
    def show(self):
        print("pen")

class pencil:
    def show(self):
        print("pencil")

obj=pencil()
obj.show()


# ----type 2 polymorphism--------duck typing-----------
print("--------------")
class pen:
    def show(self):
        print("pen")

class pencil:
    def show(self):
        print("pencil")

obj=pencil()
obj1=pen()

obj.show()
obj1.show()


# =======================ENCAPSULATION=============
# ATTRIBUTE YA METHOD K AGE  _ LGA DENE SE PROTECTED HO JATA H  TO CHILD CLASS ACCESS NHI KR SKTA WITHOUR _KA USE KIE  ,--->PR YE PYHTON M KAAM NHI KRTA BAKI SB LANGUAGE M KRTA H 

# PROTECTED
class pen:
    _a="ayush"
    def show(self):
        print("pen")

class pencil(pen):
    
    def show(self):
        # print(super().a)  #not work
        print(super()._a)
print("_______________")
obj=pencil()
obj.show()


# PRIVATE --> 2__   ab isko koi access nhi ke skta 

class pen:
    __a="ayush"
    def show(self):
        print("pen")

class pencil(pen):
  '''  
#   show error
    def show(self):
        print(super().__a)
print("_______________")
obj=pencil()
obj.show()
'''

## ________________--
#  only class k through access hoga

class Name:
    __b="ayush"
    def show(self):
        print(Name.__b)


print("_______________")
obj5=Name()
obj5.show()

#  normal attribute aur method public hote h to koi bhi change kr skta hh 







