# 1)find the biggest number
# a=int(input("enter first no"))
# b=int(input("enter the second no"))
# c=int(input("enter the third no"))
#
# if (a>b) and (a>c):
#    print("biggest is=",a)
# elif (b>a) and (b>c):
#     print("biggest is=", b)
#
# elif (c>a) and (c>b):
#     print("biggest is=", c)
# a=[1,45,678,34,987]
# b=0
# for i in a:
#     if i>b :
#         b=i
# print(b)

# 3)Create a string from the given string where the first and last character are exchanged.
# Eg: Python ⇒ nythoP

# def swap(str, i, j):
#    list1 = list(str)
#    list1[i], list1[j] = list1[j], list1[i]
#    return ''.join(list1)
# a='python'
# b=list(a)
# print(b)
# c=a[0]
# a[0]= a[-1]
# a[-1]=c
# a="string"
# b=list(a)
# print(b)
# c=b[0]
# b[0]=b[-1]
# b[-1]=c
# print(b)
# print(''.join(b))

#
# string = "hello"
# print(swap(string, 0, 4))
#
# 2) Accept an integer n and compute n+nn+nnn.
# # [Hint : n = 5, then compute 5 + 55 + 555]
#
# n = int(input("Enter a number,n="))
# nn = n*10+n
# nnn = n*100+nn
# print("n+nn+nnn=",'{}+{}+{}'.format(n,nn,nnn))

#
# 4)Write a program to prompt the user for a list of integers. For all values greater than 100,
# # store ‘over’ instead.
# list1=[45,64,123,142,98,241,54]
# for i in list1:
#     if i>100 :
#         a=list1.index(i)
#         list1[a]='over'
# print(list1)





# list1=[1,2,3,4,5,6,7,8]
# for x in list1:
#     print(x)
#     if x%2==0 :
#         print(x)
#
# list1=["salam","aslam","basim"]
# count=0
# for x in list1:
#     for y in x:
#         if y=='s':
#             count=count+1
# print("occurances=", count)

# list1=[1,2,1,4,5,6]
# list2=[6,5,4,3,2,5]
# print(list1,list2)
# for x in list1:
#     print(x)
# for y in list2:
#     print(y)
#     if len(x)=len(y):

#
# list1=[]
# n=int(input("enter range="))
# for i in range(n):
#     a=int(input("enter num="))
#     list1.append(a)
# print(list1)
#
#
# list2=[]
# num=int(input("enter range="))
#
# for i in range(num):
#     b=int(input("enter num="))
#     list2.append(b)
# print(list2)

# if len(list1)==len(list2):
#     print("same")
# else:
#     print("not same")
# sum=0
# for i in list1:
#     sum=sum+i
# print(sum)
# sum2=0
# for i in list2:
#     sum2=sum2+i
#
# print(sum2)
# if sum==sum2:
#     print("sum is same")
# else:
#     print("sum is not same")
#
# for i in list1:
#     for x in list2:
#         if x==i:
#             print("occure")
#
# a=["salim","hari","adul","lalu"]
# for i in a:
#     for x in i:
#         print(x)

# a=input("enter a line=")
# c=a.split()
# print(a)
# b={}
# for i in c:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)

# 8)Get a string from an input string where all occurrences of the first character are replaced
# # with ‘$’, except the first character. [eg: onion -> oni$n]

# a="everyone"
# b=a[0]
# c=a.replace(b,'$')
# print(b+c[1:])

# 9)Create a single string separated with space from two strings by swapping the character
# # at position 1.

# a="hello"
# b="world"
# c=a[1]
# f=b[1]
# d=a.replace(c,f)
# s=b.replace(f,c)
# print(d+s)

# 10)Write a python program to read two lists color-list1 and color-list2. Print out all colors
# # from color-list1 not contained in color-list2.

# a=[]
# x=int(input("range="))
# b=[]
# y=int(input("range="))
# for i in range(x):
#     c=input("enter-color=")
#     a.append(c)
# print(a)
# for f in range(y):
#     d=input("enter-color=")
#     b.append(d)
# print(b)
# for i in a:
#     if i in b:
#         pass
#     else:
#         print(i)

# 11)Create a list of colors from comma-separated color names entered by the user. Display
# # first and last colors

# a=input("list-color=")
# c=a.split()
# print(c[0],c[-1])

# 12)From a list of integers, create a list after removing even numbers.

# a=[]
# b=int(input("range="))
# for i in range(b):
#     c=int(input("enter nums="))
#     if c%2==0:
#         pass
#     else:
#         a.append(c)
# print(a)

# 13)Count the number of characters (character frequency) in a string.

# a=input("enter nums=")
# b={}
# cound=0
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)

# 14)Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’

# a=input("enter string=")
# if a[-3:]=="ing":
#     b=a.replace(a[-3:],"ly")
#     print(b)
# else:
#     c=a+"ing"
#     print(c)

# 15)Accept a list of words and return the length of the longest word.

a=["everyone","gohhjjkliouyod",'tohvfktjdewretutyfkhgfjt']
b=0
c=''
for i in a:
    if b<len(i):
        b=len(i)
        c=i
print(c)
print(b)

















