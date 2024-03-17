list1 = [1,2,3,4,4]
def removeValue(list, val):
   return [value for value in list if value != val]
list1.sort()
list1 = removeValue(list1, max(list1))
print(list1)
print(list1[- 1])
