#method overloading
class calculation:
    def add(self, a: int, b: int):
        print(a + b)

    def add(self, a: int, b:int, c: int = 0):
        print(a + b + c)

cal = calculation()
cal.add(2,3)
cal.add(4, 5, 6)

#method overriding
class Employee:
    __sal = 30000
    def salary(self):
        return self.__sal * 12

class contractEmployee:
    __hrpay = 300
    __hrs = 8
    def salary(self):
        return self.__hrpay * self.__hrs

emp = Employee()
print(emp.salary())
emp = contractEmployee()
print(emp.salary())


#CONSRUCTORS
#default consructor
class Student:
    def fullName(self, fname, lname):
        print(fname + lname )

std = Student()
std.fullName("prasad", "aketi25")


#parameterless constructor
class Student:
    def __init__(self):
        pass

        def fullName(self, fname, lname):
            print(fname + lname)

    std = Student()
    std.fullName("prasad", "aketi25")

#parameterized constructor
class Address:
    __dno : int = ""
    __city : str = ""
    __state : str = ""
    __country : str = ""

    def __init__(self, dno, city, state, country):
        self.__dno = dno
        self.__city = city
        self.__state = state
        self.__country = country

    def fullAdrs(self):
        print(self.__dno,self.__city, self.__state, self.__country)

adrs = Address("5-90", "palakol", "ap", "india")
adrs.fullAdrs()

