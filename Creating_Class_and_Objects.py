#**CLASS & FUNCTIONS**
# Class means a blueprint of code which consists of a functions and methods.


#constructor -> objects

class www:
    name="dinesh"
    id=23

x=www() # a variable , assigned to a class -> object/instance

x

x.name , x.id    #=> Object variable

dir(www)

dir(str)

a="asdf"

print(type(a))

www()

dir(www)

class emp:#2
    def __init__(self,id,name,age): #3 self=e1,id=2333,name=gowri,age=32
        self.ID=id #4 e1.ID = 2333
        self.Name=name #5 e1.Name=gowri
        self.Age=age #6 e1.Age=32
    location="salem" #7 e1.location=salem

e1=emp(2333,"gowri",32) #1 creates obj e1 based on emp go to __init__ #8 sucess

e1

e1.ID,e1.Name,e1.location,e1.Age

class emp:
    def __init__(self,id,name,age):
        self.ID=id
        self.Name=name
        self.Age=age
    def show(aaa):#2 aaa=e1
        print(aaa.ID,aaa.Name,aaa.Age,aaa) #3 e1.ID,e1.Name,e1.Age
    location="salem"

e1=emp(2333,"gowri",32)

e1

e1.show() #1 calls show() #4 sucess

e2=emp(1234,"adhi",12)
e2

e2.show()

e1.__init__(6789,"hameesh",22)

e1.show()

class emp:
    def __init__(self,id,name,age):
        self.ID=id
        self.Name=name
        self.Age=age
    def show(aaa):#2 aaa=e1
        print(aaa.ID,aaa.Name,aaa.Age,aaa)
    def modify(self,new_name):#2 self=e1,new_name=vishnu
        self.Name=new_name #3 e1.Name=vishnu

e1=emp(2333,"gowri",32)

e1.show()

e1.modify("vishnu") #1 call #4 sucess

e1.show()

class emp:
    def __init__(self,id,name,age):
        self.ID=id
        self.Name=name
        self.Age=age
    def show(aaa):
        print(aaa.ID,aaa.Name,aaa.Age,aaa)
    def modify(self,new_name):
        self.Name=new_name
class guvi(emp):
    pass          #PASS: is a placeholder, we use 'pass' when the function has not need to do anything.
                  #This is helpful when you are in the early stages of development and are still planning the program's structure.

e3=guvi(1222,"suresh",54)

e3.show()

class emp:
    def __init__(self,id,name,age):
        self.ID=id
        self.Name=name
        self.Age=age
    def show(aaa):
        print(aaa.ID,aaa.Name,aaa.Age,aaa)
    def modify(self,new_name):
        self.Name=new_name
class guvi(emp):
    def show(self):
        print("G"+str(self.ID),self.Name,self.Age)

e4=guvi(1222,"suresh",54)

e4.show()

class emp:
    def __init__(self,id,name,age):
        self.ID=id
        self.Name=name
        self.Age=age
    def show(aaa):
        print(aaa.ID,aaa.Name,aaa.Age,aaa)
    def modify(self,new_name):
        self.Name=new_name
class tcs(emp):
    def addLocation(self,location):
        self.loc=location
    def show(self):
        print("name",self.Name,"\nid","T"+str(self.ID),"\nage",self.Age,"\nlocation",self.loc)
class hcl(emp):  # Here hcl class(child class) inherits the attributes and methods of the emp class(parent class).
    def show(self):
        print("name",self.Name,"\nid","H"+str(self.ID),"\nage",self.Age)


e5=emp(1111,"badri",34)
e5.show()

e6=tcs(1111,"badri",34)
e6.addLocation("chennai")
e6.show()

e7=hcl(1111,"badri",34)
e7.show()
