def insert_squares(arr, num):
	x = 1
	while x <= num:
		arr.append(x**2)
		x+= 1
	return arr