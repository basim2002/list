list1=list(("hello","world","2022","1","2","3",4,5,6))
print(list1) #shows just like a complete list
print(list1[-6:-1])#can be adjust list line from the negative side or end side
print(list1[::-1])#reverse the list
print(list1[:-6])#adjust a list from where to start
print(list1[0:8:3])#skipping the middile ones based on the third value we set



list1[1:4]=["basim","aslam","a"]#changing what we set with the list line
print(list1)

list1.insert(2,"hi")#insert to list line
print(list1)

list1.append("word")#to add
print(list1)

list2=["a","b","c"]
print(list2)

list2.extend(list1)
print(list2)

list2.insert(2,"a")
print(list2)
list2.remove("a")
print(list2)
list2.pop()
print(list2)
list2.pop()
print(list2)
list2.pop()
print(list2)

del list2[1:6]
print(list2)

list1.clear()
print(list1)

del list1
print(list1)






