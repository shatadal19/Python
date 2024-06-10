class Math:
    def __init__(self,num):
        self.num = num

    def additiion(self, n):
        self.num=self.num+n

    @staticmethod
    def add(a, b):
        return a+b
    
# result = Math.add(1, 2)
# print(result)
a = Math(5)
print(a.num)
a.additiion(6)
print(a.num)