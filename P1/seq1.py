class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

class Gene(Seq):


    pass



#-- Main program
s1 = Seq("AACGTC")
g= Gene("AACGTC")
s2 = Seq("CCGTCA")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {g}")
print(f"the lengh of the sequence 1 is {s1.len()} ")
print(f"the lengh of the sequence 2 is {g.len()}")
print("testing objects")