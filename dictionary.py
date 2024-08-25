dict  = {'name': "Utpal", 'std':"4th year", 'math':87, 'english':93, 'coding': 98}

# print(dict)
# print(*dict)

# dict['name'] = "pd"

# for key in dict :
#     print(key)

# for value in dict.values():
#     print(value)

# for key in dict:
#     print(dict[key])

# print("Dictionary : \n",dict)

# print("To insert an element with key math and value 90")
# dict['maths'] = 90

# print("Dictionary : \n",dict)

# print("To insert an element with key 'name' and value 'kunal'")
# dict['name'] = "kunal"

# print("Dictionary : \n",dict)

# dict.pop()     #raise an exception : TypeError

# dict.pop('math')   #keyError

# dict.popitem()


print("Dictionary : \n",dict)

# print("To fetch keys of all elements ")

# elementIndex = dict.keys()

# print(elementIndex)

# print("To fetch values of all elements :")

# elementValues = dict.values()

# print(elementValues)

# for value in dict.values():
#     print(value , end=' ')

# elements = dict.items()
# print(elements)

# print("To retrieve value of element with key 'hindi' : ")
# print(dict.get('math',"Element does not exist"))
# print(dict.get('science',"Element does not exist"))

dict2 = {'math': 92, 'hindi': 89, 'name': 'Kunal', 'rollNo': 64}

print("Inserting all elements of dict2 in dict : ")
dict.update(dict2)

print("After inserting elements of second into first : ")
print(dict)