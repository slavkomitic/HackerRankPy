def equalize_array(arr):
	"""
	@https://www.hackerrank.com/challenges/equality-in-a-array/problem
	"""
	items = dict()
	size = len(arr)
	max_count = 1
	for n in arr:
		if current:=items.get(n, False):
			if current >= max_count:
				max_count = current + 1
			items[n] += 1
		else:
			items[n] = 1
	return size - max_count


if __name__ == "__main__":
	arr = [1, 2, 3, 1, 2, 3, 3, 3]
	#print(False>=0)
	print(equalize_array(arr))
	arr = [37, 32, 97, 35, 76, 62]
	print(equalize_array(arr))