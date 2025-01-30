#Write a Python program to create a Python list of your favourite fruits (minimum 5). Then perform the given operations on it.
fruits=['bananas','kiwi','apple','pineapple','watermelon']
print(fruits)

#sorting
fruits.sort()
print ("The sorted list is ",fruits)

#reversing
fruits.reverse()
print("The reversed list is ",fruits)

#slicing
print(fruits[1:4])

fruits.append("strawberry")
print(fruits)

print("The length of the list is ",len(fruits))

fruits.remove("kiwi")
print("Updated list is ",fruits)

fruits.clear()
print(fruits)
