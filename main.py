import random
def use(f):
    usage=1

    def using(self,*args, **kwargs):
        nonlocal usage
        self.usage+=usage
        message = "investigating info"
        result = f(self,*args, **kwargs)
        return message + "\n" + result
    return using
def creator(func):
    def is_creator(self):

        return func(self)
    return is_creator
class Language:
    usage:int
    def __init__(self, name, is_complex, usage,author,age):
        self.name = name
        self.is_complex = is_complex
        self.usage = usage
        self.author = author
        self.age = age

    @use
    def used(self):
        info=f'{self.name} is used  {self.usage}'

        return info

    def info(self):
        info= (self.name,self.is_complex,self.usage,self.author,self.age)
        return "Name: "+ str(info[0])+","+"Is complex: "+str(info[1])+","+"Used:"+str(info[2])+","+""+str(info[3])+" "+str(info[4])

    def master(self):
        chance=random.randint(0,100)
        result= ("You mastered it!" if chance >= 80
              else "You are getting there!" if chance >= 50
              else "You haven't mastered it yet!")
        return result
    @creator
    def created_by(self):
        return f"Hello,{self.author}!!!"



p=Language("Python",True,100,"Rossym",120)
print(p.used())
print(p.info())
print(p.master())
print(p.created_by())
c=Language("C++",True,100,"Stroustrup",47)
print(c.used())
print(c.info())
print(c.master())
print(c.created_by())
dotnet=Language("DotNet",True,100,"Hejlsberg",24)
print(c.used())
print(c.info())
print(c.master())
print(c.created_by())
