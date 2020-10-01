def size_of_str(str):
	return len(str)

# return size of string

def concat_strings(first, second):
	return first + second


# return concatination of first and second strings

def duplicate_string(str, copy):
	str *= copy
	return str


# return new string which is copy of str copy times
# example -> duplicate_string('s', 2) == 'ss'

def reverse(str):
	return str[::-1]


# return reverse of the string

def is_substring(str, substr):
	if substr in str:
		return True
	else: return False
