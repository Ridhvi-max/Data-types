class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class Emplyee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,idnumber)
a=Emplyee('Rahul',886012, 200000, "Intern")
a.display()