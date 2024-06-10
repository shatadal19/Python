class Employ:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} And company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
            cls.company = newCompany


e1 = Employ()
e1.name = "Shatadal"
e1.show()
e1.changeCompany("Tesla")
e1.show()