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

class Animal:
    name="lion"   #class attribute

    def __init__(self,age):
        self.age=age  # instance attribute
     
    def show(self): # instance method
        pass

#  CLASS M SIRF INSTANCE METHOD HI BNTE H KYUKI  JB BHI KOI FUNCTION DECLARE KRTE H CLASS M TO USME SELF PASS KRNE SE INSTANCE CREATE HO JATA H 

#  self targets the instace

