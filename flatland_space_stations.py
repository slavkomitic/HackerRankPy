from bisect import bisect

def flatland_space_stations(n, c):
	"""
	https://www.hackerrank.com/challenges/flatland-space-stations/problem
	"""
	cities = set([city for city in range(n)])
	cities = cities.difference(set(c))
	size = len(c)
	c = sorted(c)

	if len(cities) == 0:
		return 0

	distances = list()
	for i, city in enumerate(cities):
		index = bisect(c, city)
		if index == 0:
			distances.append(abs(city-c[0]))
		elif index == size:
			distances.append(abs(city-c[-1]))
		else:
			distances.append(min(abs(city-c[index-1]), abs(city-c[index])))

	return max(distances)


if __name__ == '__main__':

	n = 90
	c = list(map(int,"4 76 16 71 56 7 77 31 2 66 12 32 57 11 19 14 42".rstrip().split()))

	print(flatland_space_stations(n ,c))