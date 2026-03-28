#  Decorator is a function Add modifies another function. 

def decorate(func):
    def wrapper():
        print("ayush")
        func()
        print("lucky")
    return wrapper
@decorate
def hello():
    print("hii thats my name")
hello()
#### =======================================

def decorate(func):   # ye decorate parameter m   hello fuction accept krta h 
    def wrapper(a,b):   ## ye wrapper func hello ka para meter accept krta h 
        print("add of num is ")
        func(a,b)
        print(" only")
    return wrapper
@decorate
def hello(a,b):
    print(a+b)
hello(2,7)

##===================*args============

def addition(*args):  # *variavle_name  or *args accepts n number of input in tuple form   isko * se mtlb h  
    sum=0
    for i in args:
        sum +=i
    print(sum)
addition(234,23,41234,4334,5,435,4345,43,5,43,5654,2345678)

##===========**kwargs===key,value arguments==========

def addition(**kwargs):  # *variable_name  or *args accepts n number of input in dictionary form  isko kevall ** se mtlb h  
    print(kwargs)


addition(a=12,b=32,c=4,d="ayush",age=22)

##### GENERAL FORM =======================

def decorate(func):   # ye decorate parameter m   hello fuction accept krta h 
    def wrapper(*args,**kwargs):   ## ye wrapper func hello ka para meter accept krta h 
        print("add of num is ")
        func(*args,**kwargs)
        print(" only")
    return wrapper
@decorate
def hello(a,b):
    print(a+b)
hello(2,7) 




####  TERNARY OPERATOR AND LIST COMPREHENSION
a=13
print("even") if a%2==0 else print("odd")



####  TERNARY OPERATOR AND LIST COMPREHENSION
a=13
print("even") if a%2==0 else print("odd")
 
l=[i for i in range(1,21) if i%2==0 ]
print(l)


m= { j:j**2 for j in range(1,10)}
print(m)



#  LAMBDA FUNCTION=================== 
addition=lambda a,b:a+b
print(addition(2,3 ))


check=lambda a: "even" if a%2==0 else "odd"
print(check(4))

# =========MAP========
a=[2,234,53,54,3,45,3,2,6]
square=map(lambda x:x**2,a)
print(list(square))

# FILTER=========================
x=[2,234,53,54,3,45,3,2,6]
def even(x):
    if x%2==0:
        return True
    else:
        return False
fil=filter(even,a )
print(list(fil))



result=filter(lambda x:True if x%2==0 else False,x)
print(list(result))
