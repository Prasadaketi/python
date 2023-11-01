#example of abstraction
class address:
    _village : str = "abc"
    _state : str = "ap"
    _dist: str = "west godavari"
    def fullAddress(self):
        return self._dist + " " + self._state + " " + self._village
adrs = address()
adrs._dist = "bcd"
print(adrs.fullAddress())


#variable scope wrt class
#public scope
class address:
    village : str = "abc"
    state : str = "ap"
    dist: str = "west godavari"

adrs = address()
print(adrs.state)

#variable scope wrt function
#global function
def fullname():
    global fname
    fname = "prasad25"
    lname = "aketi"
fullname()
print(fname)
print(lname)
