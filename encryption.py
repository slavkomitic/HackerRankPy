import math

def encryption(s):
	"""
	@https://www.hackerrank.com/challenges/encryption
	"""
	sqrt = len(s)**0.5
	floor, ceil = math.floor(sqrt), math.ceil(sqrt)

	result = ""
	for r in range(ceil):
		for n in range(0, len(s)-r, ceil):
			result += s[r+n]
		result += " "
	return result

		

if __name__ == "__main__":
	text = "haveaniceday"
	print(encryption(text))

	text = "feedthedog"
	print(encryption(text))	

	text = "wclwfoznbmyycxvaxagjhtexdkwjqhlojykopldsxesbbnezqmixfpujbssrbfhlgubvfhpfliimvmnny"
	print(encryption(text))	