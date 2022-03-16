def binary_search(list,target):
 first = 0
 last =len(list) - 1

 while first <= last:
  midpoint = (first+last)//2
  if list[midpoint] == target:
       return midpoint
  elif list[midpoint] < target:
       first = midpoint + 1
  else: 
       last = midpoint -1
 return None

def verify(index):
  if index is not None:
    print("index is equal to", index)
  else:
    print("target not present in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers,11)
verify(result)

result = binary_search(numbers,6)
verify(result)



