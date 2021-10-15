def find_digits(n):
	"""
	@https://www.hackerrank.com/challenges/find-digits/problem
	"""
	return sum([1 for d in str(n) if int(d) and ((n % int(d)) == 0)])

if __name__ == "__main__":

	print(find_digits(111))