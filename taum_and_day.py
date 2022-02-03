def taum_and_bday(b, w, bc, wc, z):
	"""
	https://www.hackerrank.com/challenges/taum-and-bday/problem?isFullScreen=true
	"""
	if (p:=bc + z) < wc:
		wc = p
	if (p:=wc + z) < bc:
		bc = p		
	
	return w * wc + b * bc




if __name__ == '__main__':
	b = 3
	w = 5
	bc = 3 
	wc = 4
	z = 1

	print(taum_and_bday(b, w, bc, wc, z))