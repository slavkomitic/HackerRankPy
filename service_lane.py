def service_lane(n, cases):
	"""
	https://www.hackerrank.com/challenges/service-lane/problem
	"""
	return [min(width[c[0]:c[1]+1]) for c in cases]

	

if __name__ == '__main__':
		
	width = [2, 3, 1, 2, 3, 2, 3, 3]
	cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
	print(service_lane(width, cases))