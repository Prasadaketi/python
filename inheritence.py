class Address:
    __address: str = ""

    def addAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address

class Employee(Address):
    __firstname : str = ""
    __lastname : str = ""
    __surname : str = ""

    def setName(self, fname, lname, sname):
       self.__firstname = fname
       self.__lastname = lname
       self.__surname = sname
    def __nameFormat(self):
        return f'{self.__firstname} {self.__lastname} {self.__surname}'

    def getFullname(self):
        return self.__nameFormat()


emp = Employee()
emp.setName(fname = "prasad", lname = "aketi", sname = "25")
emp.addAddress("Yelamanchili")
print(emp.getFullname())
print(emp.getAddress())