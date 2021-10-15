def cut_the_sticks(sticks):
	"""
	@https://www.hackerrank.com/challenges/cut-the-sticks/problem
	"""
	cuts = list()

	while len(sticks) > 0:
		short = min(sticks)
		cuts.append(len(sticks))
		sticks = [n-short for n in sticks if (n-short)>0]
		

	return cuts

if __name__ == "__main__":

	sticks = [int(n) for n in "5 4 4 2 2 8".split()]
	print(cut_the_sticks(sticks))