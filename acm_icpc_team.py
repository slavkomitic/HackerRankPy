import random

from itertools import combinations
def acm_icpc_team(topics):
	"""
	@https://www.hackerrank.com/challenges/acm-icpc-team/problem
	"""

	topics = [[int(n) for n in list(t)] for t in topics]
	result  = [sum([x[0] or x[1] for x in list(zip(*t))]) for t in combinations(topics, 2)]
	return [top:=max(result), result.count(top)] 

if __name__ == "__main__":
	topics = [''.join([str(random.randint(0, 1)) for n in range(500)]) for m in range(500)]
	print(acm_icpc_team(topics))