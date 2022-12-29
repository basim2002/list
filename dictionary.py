dic1={"one":1,"two":2,3:"three"}
print(dic1)
# print(dic1["two"])
# print(dic1[3])
# dic1["two"]=11
# print(dic1)
# dic1["four"]=4
# print(dic1)
# dic1.pop("two")
# print(dic1)
# del dic1[3]
# print(dic1)
# print(len(dic1))
# dic1["one"]=["hi","everyone",9,10]
# print(dic1)
# print(dic1.get("one"))
# print(dic1.keys())#to list keys
# print(dic1.values())#to list values
# print(dic1.items())
# dic1.update({"four":4444})
# print(dic1)
# # dic1.clear()
# # print(dic1)
# dic1.popitem()
# print(dic1)
dic2={5:"five",6:"six"}
print(dic2)
dic3={7:"seven",8:"eight"}
print(dic3)
dic4={"dic1":dic1,"dic2":dic2,"dic3":dic3}
print(dic4)
print(dic4.keys())
print(dic4.values())
print(dic4.get("dic2"))
# dic4["dic2"]=[1,2,3,4]
# print(dic4)
# dic4[5]=[1,2]
print(dic4)
dic4['dic2'][5]='hello'
print(dic4)
dic4['dic3'][8]="hi"
print(dic4)
dic4.pop("d")
print(dic4)

