#function with optional parameters
def sub(literal1: int, literal2: int, literal3: int = 0):
    print(literal1 - literal2 - literal3)

sub(30, 5,)
sub(30, 5, 3)


#function with arbitary paramerters
def add(* literals):
    res : int = 0
    for items in literals:
        res += items
    print(res)
add(50, 10, 5, 15, 6, 10, 2)

#function with arbitary keyparameters
def address(** literals):
    dno = literals.get("dno")
    street = literals.get("street")
    village = literals.get("village")
    dist = literals.get("dist")
    state = literals.get("state")
    country =literals.get("country")
    print(dno, street, village, dist, state, country)

address(dno = "123", street = "abc", village = "bcd", dist = "xyz", state = "ap")

#returnable function
def add(literal1: int, literal2: int, literal3: int = 0):
    return literal1 + literal2 + literal3
result = add(20, 5)
print(result)
