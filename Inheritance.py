class fruit:

    def __init__(self,type1):
        self.type1=type1

    def taste1(self,type1):
        self.type1=type1
        print(self.type1)

class veg(fruit):
    def __init__(self,type2):
        fruit.__init__(self,type2)
        self.type2=type2


    def taste2(self,type2):
        self.type2=type2
        print(self.type2)
        print(self.type1)


# class lemon(fruit,veg):
#     def __init__(self):
#         self.type="bitter fruit"
#     def taste3(self,bitter):
#         self.bitter=bitter
#         print(self.bitter)

c=veg('banana')
c.taste2('apple')


# d=veg()
