class Persion:
    name = "Shatadal"
    occ = "Deveploper"

    def __init__(self, n, o):
        print("Hey, I am a persion")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Persion("Shatadal" , "Developer")
b = Persion("Dibba" , "Self Employee")
c = Persion(2,3)
a.info()
b.info()
c.info()
# a.name = "Dibba"
# a.occ = "Self emplpy"
# a.info()
# b.info()