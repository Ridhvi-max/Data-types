class myClass:
    __privateVar=27
    def __privateMeth(self):
        print("I'm inside class myClass")
    def hello(self):
        print("Private Variable value: ",myClass.__privateVar)
foo=myClass()
foo.hello()
foo.__privateMeth