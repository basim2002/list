# a=input("word=")
# b=a.split()
# print(a)
# c={}
# for i in b:
#     if i in c:
#         c[i]+=1
#     else:
#         c[i]=1
# print(c)


# a=[2,-3,-4,5,-1,8]
# b=[x for x in a if x>0]
# print(b)

# b=[n**2 for n in range(11)]
# print(b)

# a=input("enter a word=")
# c="aeiou"
# b=[x for x in a if x in c]
# print(b)


# sum=0
# a=[2,5,7,4,9,2]
# for i in range(0,len(a)):
#     sum=sum+a[i]
# print(sum)

# a={"morning":"breakfast","noon":"snacks"}
# b={"afternoon":"lunch","evening":"snacks"}
# c={}
# c=a.copy()
# for key,value in b.items():
#     c[key]=value
# print(c)

# a=int(input("enter num="))
# factorial=1
# for i in range(1,a+1):
#     factorial=factorial*i
# print(factorial)

# n1=0
# n2=1
# for i in range(7):
#     print(n1)
#     n3 = n1 + n2
#     n1=n2
#     n2=n3

# a=int(input("enter num="))
# n1=0
# n2=1
# i=0
# while (a>i) :
#     print(n1)
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     i=i+1



# a=int(input("enter num="))
# for i in range(1,11):
#    print(i,'*',a,'=',i*a)

# a=int(input("enter num="))
# b=1
# for i in range(1,4):
#     b=
# print(b)

# a=[]
# for i in range(1000,10000):
#     if i%2==0 and a**2==

# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i * j ,end=" ")
#     print()


# find number of upper case and lower case letters in a user given word
# a=input("type word=")
# b=0
# c=0
# for i in a:
#     if (i>="a" and i<="z"):
#         b=b+1
#     if (i>="A" and i<="Z"):
#         c=c+1
#         print("number of lower case are=",b)
#         print("number of upper case are=",c)

# a=input("type word=")
# lower=0
# upper=0
# for i in a:
#     if (i.isupper()):
#         upper+=1
#     else:
#         lower+=1
# print("upper case=",upper )
# print("lower case=",lower)


# a=[i**2 for i in range(1,21)]
# print(a)

# for char in string.printable[-2:]:
#     print(char, '-', ord(char))


# for i in range(4):
#     for j in range(4):
#         print('*',end=' ')
#     print()
#
# for i in range(4):
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
#
# for i in range(4):
#     for j in range(i,4):
#         print('*',end=' ')
#     print()
#
# for i in range(4):
#     for j in range(i,4):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('* ',end='')
#     print()
#
# for i in range(4):
#     for j in range(i+1):
#         print(' ',end=' ')
#     for j in range(i,4):
#         print('*',end=' ')
#     print()
#
# for i in range(4):
#     for j in range(i,4):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
#
# for i in range(4):
#     for j in range(i+1):
#         print(' ', end=' ')
#     for j in range(i,4):
#         print(' * ', end=' ')
#     print()

# for i in range(5):
#     for j in range(1,i+1):
#         print(i*j,end=' ')
#     print()

# 1)

for i in range(5):
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(5):
    for j in range(i,5):
        print('*',end=' ')
    print()

# 2)

for i in range(5):
    for j in range(i,5):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()

# 3)

for i in range(5):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,5):
        print('*',end=' ')
    for j in range(i,4):
        print('*',end=' ')
    print()

# 4)

for i in range(4):
    for j in range(i,5):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(5):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,5):
        print('*',end=' ')
    for j in range(i,4):
        print('*',end=' ')
    print()

# 5)

for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    print()

# 6)

for i in range(i):
    for j in range(i):
        print(i,end=' ')
    print()


# n= 2345
# i=(n%10)
# while i%2 !=0:
#     continue
# print(n)
# print(i)
