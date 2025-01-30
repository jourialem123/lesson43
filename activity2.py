mydict={"name":"Jouri","age":16}
print(mydict)

mydict["grade"]=1

print("Updated dictionary is ",mydict)

print("My name is ",mydict["name"])
mydict.pop("age")

print("updated dictionary is ",mydict)

mydict.clear()
print(mydict)