# Matrix Tools
# by Kanishka_Developer

def btfy(matrix, maxLength): # beautifies matrix for easier viewing
	op = ""
	for l in list(matrix):
		if l != matrix[len(matrix)-1]:
			x = ""
			for i in list(l):
				if i != matrix[len(matrix)-1]:
					s = " "
					for v in range(0, maxLength + 1 - len(str(i))):
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
					for v in range(0, maxLength + 1 - len(str(i))):
						s = s + " "
					x = x + str(i) + s
				else:
					x = x + str(i)
			op = op + x
	return "\n" + op + "\n"

def rt90CW(matrix, maxLength):
	rC = len(matrix)
	cC = len(matrix[0])
	print("Matrix:\n{}".format(btfy(matrix, maxLength)))
	print("Matrix size: {} x {}".format(cC, rC))
	rC, cC = cC, rC
	nMatrix = []
	for i in range(0, rC):
		row = []
		for j in range(cC-1, -1, -1):
			row.append(matrix[j][i])
		nMatrix.append(row)
	return nMatrix

def rt90AC(matrix, maxLength):
	rC = len(matrix)
	cC = len(matrix[0])
	print("Matrix:\n{}".format(btfy(matrix, maxLength)))
	print("Matrix size: {} x {}".format(cC, rC))
	rC, cC = cC, rC
	nMatrix = []
	for i in range(rC-1, -1, -1):
		row = []
		for j in range(0,cC):
			row.append(matrix[j][i])
		nMatrix.append(row)
	return nMatrix

def rtCW(matrix, maxLength):
	rC = len(matrix)
	cC = len(matrix[0])
	print("Matrix:\n{}".format(btfy(matrix, maxLength)))
	print("Matrix size: {} x {}".format(cC, rC)) # you're screwed if input isn't an nxn matrix. trust me on that one.
	lC = int(max(rC,  cC) / 2) if max(rC,  cC) % 2 == 0 else int((max(rC, cC) - 1) / 2)
	for l in range(1, lC+1):
		for i in range(l-1, rC-l):
			matrix[i].insert(l-1, matrix[i+1].pop(l-1))
		for i in range(rC-l, l-1, -1):
			matrix[i].insert(cC-l, (matrix[i-1].pop(cC-l))) if (i != l) else matrix[i].insert(cC-l, (matrix[i-1].pop(cC-l+1)))
	return matrix

def rtAC(matrix, maxLength):
	rC = len(matrix)
	cC = len(matrix[0])
	print("Matrix:\n{}".format(btfy(matrix, maxLength)))
	print("Matrix size: {} x {}".format(cC, rC)) # you're screwed if input isn't an nxn matrix. trust me on that one.
	lC = int(max(rC,  cC) / 2) if max(rC,  cC) % 2 == 0 else int((max(rC, cC) - 1) / 2)
	for l in range(1, lC+1):
		for i in range(rC-l, l-1, -1):
			matrix[i].insert(l-1, matrix[i-1].pop(l-1))
		for i in range(l-1, rC-l):
			matrix[i].insert(cC-l, (matrix[i+1].pop(cC-l))) if (i != rC-l-1) else matrix[i].insert(cC-l, (matrix[i+1].pop(cC-l+1)))
	return matrix

def fpVT(matrix, maxLength):
	rC = len(matrix)
	cC = len(matrix[0])
	print("Matrix:\n{}".format(btfy(matrix, maxLength)))
	print("Matrix size: {} x {}".format(cC, rC))
	if rC % 2 == 0:
		l = int(rC/2)
	else:
		l = int((rC + 1)/2)
	for i in range(0, l):
		j = rC - i -1
		matrix[i], matrix[j] = matrix[j], matrix[i]
	return matrix

def fpHZ(matrix, maxLength):
	rC = len(matrix)
	cC = len(matrix[0])
	print("Matrix:\n{}".format(btfy(matrix, maxLength)))
	print("Matrix size: {} x {}".format(cC, rC))
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
matrix4x3 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # pls dont use UwU

#print(btfy(rt90CW(matrix4x4, 4), 4))
#print(btfy(rt90AC(matrix4x4, 4), 4))
#print(btfy(matrix4x4, 4))
#print(btfy(rtCW(matrix4x4, 4), 4))
#print(btfy(rtAC(matrix4x4, 4), 4))
#print(btfy(fpVT(matrix4x4, 4), 4))
#print(btfy(fpHZ(matrix4x4, 4), 4))