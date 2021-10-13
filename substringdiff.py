from dis import dis
def _print_matrix(m):
	for r in range(len(m)):
		for c in range(len(m[0])):
			print(m[r][c], end=" ")
		print()
def substringDiff(k, s1, s2):
	from time import perf_counter_ns
	timings = []

	def timer(msg):
		nonlocal timings
		timings.append(perf_counter_ns())
		if len(timings) <= 1:
			...
		else:
			print(msg, (timings[-1] - timings[-2]) / 10**6, "ms")
	#timer("start")
	n = len(s1)
	l, r1, r2 = 0, 0, 0
	size, longest = 0, 0
	matrix = [[0 for n in range(n)] for x in range(n)]
	#timer("post-set up")
	fdiag = [[] for _ in range(n + n - 1)]
	diag = [[] for ky in range(len(fdiag))]
	min_bdiag = -n + 1
	#print("diag len: ", len(diag))
	#timer("post-diag-variable set up")
	for x in range(n):
		for y in range(n):
			if s1[x] == s2[y]:
				#matrix[y][x] = 1
				diag[x-y-min_bdiag].append(1) #x-y-min_bdiag
			else:
				diag[x-y-min_bdiag].append(0)


	timer("post-build diagonals")
	
	diag = sorted(diag, key=lambda x: sum(x), reverse=True)
	maximum = sum(diag[0])
	#timer("post-sort diagonals")
	s = 0
	diag_count = int(len(diag) // 4)
	for i, d in enumerate(diag[:diag_count]):
		if (sum(d)) <= 0:
			timer("finish post looking for max string")
			return longest
		lg = len(d)
		slc = slice(0, 1)
		while size <= lg:
			a = d[slc]
			la = len(a)
			if (la - sum(a)) <= k:
				size += 1
				longest = max(longest, la)
				slc = slice(s, size)
			else:
				s += 1
				size += 1
				slc = slice(s, size)
		s, size = 0, 0

	#timer("finish post looking for max string")
	return longest
			


if __name__ == "__main__":
	from time import perf_counter_ns
	start = perf_counter_ns()
	k, s1, s2 = 0, 'abacba', 'abcaba'
	#print(substringDiff(k, s1, s2))
	k, s1, s2 = 2, 'tabriz', 'torino'
	#print(substringDiff(k, s1, s2))
	start = perf_counter_ns()
	#dis(substringDiff)
	with open("testcase8.txt", "r") as f:
		 f.readline()
		 for line in f:
			  k, s1, s2 = line.split(" ")
			  k = int(k)
			  
			  print("K: ", k, ", result: ", substringDiff(k, s1, s2))
	end = perf_counter_ns()
	print((end - start) / 10**6, "ms")