def minimum_distances(arr):
	"""
	@https://www.hackerrank.com/challenges/minimum-distances/problem
	"""
	d = sorted([(n, i) for i, n in enumerate(arr)])
	distances = [d[i][1] - d[i-1][1] for i in range(1, len(arr)) if d[i][0]==d[i-1][0]] 
	return min(distances) if distances else -1


if __name__ == '__main__':
	arr = [7, 1, 3, 4, 1, 7]
	#print(min(0, []))
	print(minimum_distances(arr))