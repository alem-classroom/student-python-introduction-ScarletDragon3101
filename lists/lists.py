def size_of_list(list_a):
	return len(list_a)


# return size of list

def add_elem_to_list(list_a, elem):
	list_a.append(elem)
	return list_a


# add elem to list and return the list

def delete_elem_from_list(list_a, index=-1):
	list_a.pop(index)
	return list_a


# delete element from list, such that its index is index

def count_elements_in_list(list_a, x):
	return list_a.count(x)


# count elements in the list that are equal to x and return the count

def sort_list(list_a):
	list_a.sort()
	return list_a


# return sorted list

def reverse(list_a):
	list_a.reverse()
	return list_a