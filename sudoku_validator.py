import math
import random

def validate_list(l):
	return sorted(l) == list(range(1,10))


def is_valid_sudoku(s_list):		
	# validate rows & columns
	for k in range(9): 	
			# validate column
			col = [s[k] for s in s_list]
			if not validate_list(col):
				print('invalid_column {}'.format(col))
				return False
			# validate row
			if not validate_list(s_list[k]):
				print('invalid row {}'.format(s_list[k]))
				return False
	
	# validate grid
	grids = [[] for r in range(9)]
	for row in range(9):
		for cell in range(9):
			grid_idx = (row - row % 3) + (math.floor(cell/3))
			grids[grid_idx].append(s_list[row][cell])

	for grid in grids:
		if not validate_list(grid):
			print('invalid grid {}'.format(grid))
			return False

	return True


if __name__ == '__main__':

	board = [[5,3,4,6,7,8,9,1,2],
			  [6,7,2,1,9,5,3,4,8],
			  [1,9,8,3,4,2,5,6,7],
			  [8,5,9,7,6,1,4,2,3],
			  [4,2,6,8,5,3,7,9,1], 
			  [7,1,3,9,2,4,8,5,6],
			  [9,6,1,5,3,7,2,8,4],
			  [2,8,7,4,1,9,6,3,5],
			  [3,4,5,2,8,6,1,7,9]] 
	is_valid_sudoku = is_valid_sudoku(board)
	print('is_valid_sudoku', is_valid_sudoku)
