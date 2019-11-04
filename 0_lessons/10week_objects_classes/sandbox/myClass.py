
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length
class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print("\t Duck's description: ",bill.description)
        print("\t Tail's length: ",tail.length)

tail = Tail("long")
bill = Bill("wide orange")
duck = Duck(bill,tail)
duck.about()
print("\t Object memory address: ",duck) # address of object's memory
