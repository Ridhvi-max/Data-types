from abc import ABC, abstractmethod
class ABsclass(ABC):
    def print(self,x):
        print("Passed value: ", x)
    def task(self):
        print("We are inside ABsclass task")
class test_class(ABsclass):
    def task(self):
         print("We are inside test_class task")
test_obj=test_class()
test_obj.task()
test_obj.print(100)
