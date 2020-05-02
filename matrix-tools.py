# Matrix Tools
# by Kanishka_Developer

def maxLength(matrix): # returns length of longest item in matrix
	maxLength = 0
	for i in range (0, len(matrix)):
		for j in range (0, len(matrix[i])):
			if len(str(matrix[i][j])) > maxLength:
				maxLength = len(str(matrix[i][j]))
	return maxLength

def btfy(matrix): # beautifies matrix for easier viewing
	mL = maxLength(matrix)
	op = ""
	for l in list(matrix):
		if l != matrix[len(matrix)-1]:
			x = ""
			for i in list(l):
				if i != matrix[len(matrix)-1]:
					s = " "
					for v in range(0, mL + 1 - len(str(i))):
						s = s + " "
					x = x + str(i) + s
				else:
					x = x + str(i)
			op = op + x + "\n"
		else:
			x = ""
			for i in list(l):
				if i != matrix[len(matrix)-1]:
					s = " "
					for v in range(0, mL + 1 - len(str(i))):
						s = s + " "
					x = x + str(i) + s
				else:
					x = x + str(i)
			op = op + x
	return "\n" + op + "\n"

def rt90CW(matrix): # rotates matrix by 90 degrees clockwise
	rC = len(matrix)
	cC = len(matrix[0])
	#print("Matrix:\n{}".format(btfy(matrix)))
	#print("Matrix size: {} x {}".format(cC, rC))
	rC, cC = cC, rC
	nMatrix = []
	for i in range(0, rC):
		row = []
		for j in range(cC-1, -1, -1):
			row.append(matrix[j][i])
		nMatrix.append(row)
	return nMatrix

def rt90AC(matrix): # rotates matrix by 90 degrees anti-clockwise
	rC = len(matrix)
	cC = len(matrix[0])
	#print("Matrix:\n{}".format(btfy(matrix)))
	#print("Matrix size: {} x {}".format(cC, rC))
	rC, cC = cC, rC
	nMatrix = []
	for i in range(rC-1, -1, -1):
		row = []
		for j in range(0,cC):
			row.append(matrix[j][i])
		nMatrix.append(row)
	return nMatrix

def rtCW(matrix): # rotates matrix by one item clockwise; works only for NxN matrices
	rC = len(matrix)
	cC = len(matrix[0])
	#print("Matrix:\n{}".format(btfy(matrix)))
	#print("Matrix size: {} x {}".format(cC, rC))
	lC = int(max(rC,  cC) / 2) if max(rC,  cC) % 2 == 0 else int((max(rC, cC) - 1) / 2)
	for l in range(1, lC+1):
		for i in range(l-1, rC-l):
			matrix[i].insert(l-1, matrix[i+1].pop(l-1))
		for i in range(rC-l, l-1, -1):
			matrix[i].insert(cC-l, (matrix[i-1].pop(cC-l))) if (i != l) else matrix[i].insert(cC-l, (matrix[i-1].pop(cC-l+1)))
	return matrix

def rtAC(matrix): # rotates matrix by one item anti-clockwise; works only for NxN matrices
	rC = len(matrix)
	cC = len(matrix[0])
	#print("Matrix:\n{}".format(btfy(matrix)))
	#print("Matrix size: {} x {}".format(cC, rC))
	lC = int(max(rC,  cC) / 2) if max(rC,  cC) % 2 == 0 else int((max(rC, cC) - 1) / 2)
	for l in range(1, lC+1):
		for i in range(rC-l, l-1, -1):
			matrix[i].insert(l-1, matrix[i-1].pop(l-1))
		for i in range(l-1, rC-l):
			matrix[i].insert(cC-l, (matrix[i+1].pop(cC-l))) if (i != rC-l-1) else matrix[i].insert(cC-l, (matrix[i+1].pop(cC-l+1)))
	return matrix

def fpVT(matrix): # flips matrix vertically
	rC = len(matrix)
	cC = len(matrix[0])
	#print("Matrix:\n{}".format(btfy(matrix)))
	#print("Matrix size: {} x {}".format(cC, rC))
	if rC % 2 == 0:
		l = int(rC/2)
	else:
		l = int((rC + 1)/2)
	for i in range(0, l):
		j = rC - i -1
		matrix[i], matrix[j] = matrix[j], matrix[i]
	return matrix

def fpHZ(matrix): # flips matrix horizontally
	rC = len(matrix)
	cC = len(matrix[0])
	#print("Matrix:\n{}".format(btfy(matrix)))
	#print("Matrix size: {} x {}".format(cC, rC))
	if cC % 2 == 0:
		l = int(cC/2)
	else:
		l = int((cC + 1)/2)
	for i in range(0, rC):
		for j in range(0, l):
			k = cC - j -1
			matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
	return matrix

matrix3x3 = [[1,2,3],[4,5,6],[7,8,9]]
matrix4x4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix4x3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] #! matrix-tools is designed primarily for NxN matrices !

#print(maxLength(matrix4x4))
#print(btfy(matrix4x4))
#print(btfy(rt90CW(matrix4x4)))
#print(btfy(rt90AC(matrix4x4)))
#print(btfy(rtCW(matrix4x4)))
#print(btfy(rtAC(matrix4x4)))
#print(btfy(fpVT(matrix4x4)))
#print(btfy(fpHZ(matrix4x4)))
