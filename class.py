# class basim:
#     def age(self):
#         c=20
#         print(c)
#
#
# a=basim()
#
# a.age()
#
# basim.age(a)
#
# class basim:
#     def age(self,c):
#         self.c=c
#
#         print(self.c)

    # def gf(self,gf1,gf2):
    #     self.gf1=gf1
    #     self.gf2=gf2
    #     print('this is my first gf',self.gf1,'This is my second gf',self.gf2,sep='\n')

# GF=basim()
# # GF.gf('aiswarya','kamala')
# GF.age(20)
#

# class fruit:
#     def __init__(self,name,taste):
#         self.name=name
#         self.taste=taste
#     def types(self):
#         print("this fruit name is",self.name)
#         print("this fruit taste like",self.taste)
#     def prize(self,high,low):
#         self.high=high
#         self.low=low
#         print('this fruit prize is',self.name,self.high)
#         print('this fruit prize is',self.name,self.low)
# c=fruit('mango','sweet')
# a=fruit('apple','good')
# c.types()
# a.types()
# c.prize('low','')
# a.prize('high','')

class apple:
    ty='fruit'
    def __init__(self,prize):
        self.prize=prize
        print(self.prize)
        self.veg= self.veg()

    def update(self):
        self.prize=50
        print(self.prize)
        self.veg.show()


    class veg:
        def __init__(self):
            self.power='high'

        def show(self):
            print(self.power)


    # @classmethod
    # def sum(cls):
    #     return cls.ty
    # @staticmethod
    # def avg(prize):
    #     return prize

# c=apple(20)
# c.update()
# a=apple(40)
# print(c.ty)
# print(c.sum())
# print(c.avg(3))
c=apple(56)
print(c.veg.power)








