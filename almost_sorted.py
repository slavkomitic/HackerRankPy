def almost_sorted(arr):
	"""
	https://www.hackerrank.com/challenges/almost-sorted/problem
	"""
	sorted_arr = sorted(arr)
	arr_size = len(arr)

	if arr == sorted_arr:
		return "yes"
	for n in range(arr_size-1):
		if arr[n+1] < arr[n]:

			if (arr[:n] + arr[n+1:n+2] + arr[n:n+1] + arr[n+2:]) == sorted_arr:
				return f"yes\nswap {n+1} {n+2}"
			else:
				next_smallest_index = n
				for k in range(n, arr_size):
					if arr[k] < arr[next_smallest_index]:
						next_smallest_index = k		
				arr[next_smallest_index], arr[n] =  arr[n], arr[next_smallest_index]
				if arr == sorted_arr:
					return f"yes\nswap {n+1} {next_smallest_index+1}" 
				else:
					arr[next_smallest_index], arr[n] =  arr[n], arr[next_smallest_index]
					if (arr[:n] + list(reversed(arr[n:next_smallest_index+1])) + arr[next_smallest_index+1:arr_size])  == sorted_arr:
						return f"yes\nreverse {n+1} {next_smallest_index+1}"
					else:
						return "no"
			


if __name__ == '__main__':
		tests =[
			[4, 2],
			[1, 3, 4, 5, 9, 7, 8, 6],
			[1, 5, 4, 3, 2, 6]
		]

		for test in tests:
			print(almost_sorted(test))
