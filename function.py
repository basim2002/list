# def hello():
#     print('Hello World')
# hello()
#
#
# def sum(a,b):
#     c=a+b
#     return c
# print(sum(3,2))



# c=lambda x : x+5
# print(c(10))

# c=lambda l,b: 1/2*l*b
# print(c(5,4))

def sum(a,b):
    c=lambda n: a*b*n
    return c
e=sum(5,4)
print(e(5))


