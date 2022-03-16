#list = [23,67,11,67,23,89,00,04,56,2,8]
#list.sort()
#print(list)
#print("smallet number from list is", list[1])


def secondsmallest(list):
	list.sort()
	print(list)
	return list[1]


A = [23,67,11,67,23,89,00,04,56,2,8]

B = secondsmallest(A)
print(B)	
