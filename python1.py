#Problem : 
#You are given a n x m matrix, which contains all the integers from 1 to n * m, inclusive, each exactly once.
#initially you are standing in the cell containing the numbe 1, On each turn you are allowed to move to an adjacent cell, i. e.
#to a cell that shares a common side with the one you are standing on now. It is prohibited to visit any cell more than once.
#Check if it is possible to visit all the cells of the matrix in the order of increasing numbers in the cells, i. e. get to the cell with the number 2 on the first turn,
# then move to 3, etc.
#Example 
# For matrix = [[1,4,5],[2,3,6]] the output should be findPath(matrix) = true;
# For matrix = [[1,3,6],[2,4,5]] the output should be findPath(matrix) = false;

def findPath(matrix):
	i = 0 
	j = 0
	k = 2
	# i , j is index for number k
	for z in range(1,(len(matrix)*len(matrix[0])+1)):
		for x in range(len(matrix)):
			for y in range(len(matrix[0])):
				# if matrix[x][y] == k, that index will be i, j
				if (matrix[x][y] == k):
					if (((i == x-1 or i == x+1) and j == y) or (i == x and (j == y-1 or j == y+1))):
						i,j = x,y
						k +=1
						#if i,j is not adjacent to x, y , print false
					else:
						return print(false)
						break;
	#else, all is true
	return print(true)


findPath([[1,3,6],[2,4,5]])
findPath([[1,4,5],[2,3,6]])