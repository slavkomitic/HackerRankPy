def sherlock_and_squares(a, b):
	"""
	@https://www.hackerrank.com/challenges/sherlock-and-squares/problem
	"""
	counter = 0
	floor = int(a**0.5)

	while(val:=floor**2) <= b:
		if val in range(a, b+1):
			counter += 1
		floor += 1
	
	return counter


if __name__ == "__main__"	:

	print(sherlock_and_squares(2, 9))
	print(sherlock_and_squares(17, 24))