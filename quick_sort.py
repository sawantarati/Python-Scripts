def quick_sort(list):
	if len(list) <= 1:
		return list
	less_than_pivot = []
	greated_than_pivot = []
	pivot = list[0]
	for i in list[1:]:
		if i <= pivot:
			less_than_pivot.append(i)
		else:
			greated_than_pivot.append(i)
	print("%15s %1s %-15s" % (less_than_pivot,pivot,greated_than_pivot))
	return quick_sort (less_than_pivot) + [pivot] + quick_sort(greated_than_pivot)
	
a_list = [55,78,34,12,89,34,67,90,100]
print(a_list)
sorted_number = quick_sort(a_list)

print(sorted_number)
