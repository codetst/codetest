import numpy as np

def funct(grid):
	x = np.array(grid)
	r= x[0].size #get row size
	c= x[:,0].size #get column size

	leastcost = np.zeros((r,c)) #zero array

	for i in range(r):
		for j in range(c):
			if i==0: #first row
				leastcost[0][j] = leastcost[0][j-1] + int(grid[0][j], 16)
			elif j==0: #first column
				leastcost[i][0] = leastcost[i-1][0] + int(grid[i][0], 16)
			else:
				leastcost[i][j] = min(leastcost[i-1][j],leastcost[i][j-1]) + int(grid[i][j], 16) #except first row and firstcolumn

	robot_path = ''
	

	while True:  #check for lesser value and assign robot_path
		if i == 0 and j == 0:
			break

		if i == 0 :
			robot_path += 'r'
			j -= 1

		elif j == 0 :
			i -= 1
			robot_path += 'd'

		elif leastcost[i-1][j] < leastcost[i][j-1]:
			robot_path += 'd'
			i-=1

		elif leastcost[i][j-1] < leastcost[i-1][j]:
			robot_path += 'r'
			j-=1

	s = ','.join (robot_path[::-1])
   
	print("robot path : %s" %s)



grid = [['46B', 'E59', 'EA', 'C1F', '45E', '63'],

          ['899', 'FFF', '926', '7AD', 'C4E', 'FFF'],

          ['E2E', '323', '6D2', '976', '83F', 'C96'],

          ['9E9', 'A8B', '9C1', '461', 'F74', 'D05'],

          ['EDD', 'E94', '5F4', 'D1D', 'D03', 'DE3'],

          ['89', '925', 'CF9', 'CA0', 'F18', '4D2']]

  
print(funct(grid))  #call function  