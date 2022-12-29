# class job:
#     def __init__(self,salary,bonus):
#         self.salary=salary
#         self.bonus=bonus
#     def sum(self,a=None,b=None,c=None):
#
#         sum=0
#         s=a+b+c
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=None and b!=None:
#             print(a+b)
#         else:
#             print(a)
#         return s
# r=job(200,10)
# r.sum(20,10,30)

# method overwriting
# class a:
#     def show(self):
#         print('hi')
#
#     def show(self):
#         print('hello')
#
#     def show(self):
#         print('hel')
# class b(a):
#     def show(self):
#         print('hello')
#
#     def show(self):
#         print('chello')
# s=b()
# s.show()

# encapsulation
# class fruit:
#     def __init__(self):
#         self.__a =5
#
# class veg(fruit)  :
#     def __init__(self):
#         self.b=3
#         fruit.__init__(self)
#         self.__b=4
# s=veg()
# print(s._fruit__a)

# operator overloading
# class prize:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __sub__(self, other):
#         a=self.a-other.a
#         b=self.b-other.b
#         s=prize(a,b)
#         return s
# c=prize(20,10)
# d=prize(15,25)
# s=c-d
#
# print(s.b)
