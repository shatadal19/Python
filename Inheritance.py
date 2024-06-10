class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def shShowDitils(self):
        print(f"The name of my employ is {self.name} and id is {self.id}")


class Programmer(employee):
    def Showlanguage(self):
        print("The diffcult language is Python")

# e = employee("Shatadal", 20)
# e.shShowDitils()
e1 = Programmer("Shatadal", 88)
e1.shShowDitils()
e1.Showlanguage()