def reverse_dict(dict):
	list_key,list_ans= [ x for x in dict.keys()],[x for x in dict.values()]
	dict = {list_ans[element]: list_key[element] for element in range(len(list_key))}
	return (dict)