''' Sudoku.py
Luxun Xu & Eden Ghirmai 
CSE415 Spr16 - 4/29/2015
Assignment 4: Problem Formulation
'''

#<METADATA>
PROBLEM_NAME = "Sudoku"
PROBLEM_AUTHORS = ['Eden Ghirmai', 'Luxun Xu']
PROBLEM_CREATION_DATE = "29-APR-2016"
PROBLEM_DESC=\
'''This formulation of the basic eight puzzle uses generic
Python 3 constructs and has been tested with Python 3.4.
It is designed to work according to the QUIET tools interface.
'''

#<COMMON_CODE>
def DEEP_EQUALS(s1, s2):
	if len(s1) != len(s2) or len(s1[0]) != len(s2[0]):
		return False

	for i in range(len(s1)):
		for j in range(len(s1)):
			if s1[i][j] != s2[i][j]:
				return False

	return True

def DESCRIBE_STATE(s):
	return render_state(s)

def HASHCODE(s):
	return str(s)

def space_occupied(s):
	result = 0
	for i in range(len(s)):
		for j in range(len(s)):
			if s[i][j] != -1:
				result += 1
	
	return result	

def copy_state(s):
	new = [[-1 for x in range(9)] for y in range(9)]
	for i in range(len(s)):
		for j in range(len(s)):
			new[i][j] = s[i][j]

	return new

def goal_test(s):
	for i in range(len(s)):
		for j in range(len(s)):
			if s[i][j] == -1:
				return False

	return True

def goal_message(s):
	return "Your Sudoku has been solved!!"


class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

def move(s, n, x, y):
	new = copy_state(s)
	new[x][y] = n
	return new


def can_move(s, n, x, y):
	if (s[x][y] != -1):
		return False

	#check row
	row = s[x]
	for num in row:
		if num == n:
			return False

	#check col
	for row in s:
		if row[y] == n:
			return False

	#check box	
	for row in range(3):
		for col in range(3):
			if(s[row + (x  - x % 3)][col + (y - y %3)] == n):
				return False

	return True


#</COMMON_CODE>

def h_euclidean(s):
  return space_occupied(s)


def h_hamming(s):
  result = 0
  for tile in s:
    if s.index(tile) != GOAL_STATE.index(tile):
      result += 1

  return result

def h_manhattan(s):
  result = 0
  for tile in s:
    goal_index = GOAL_STATE.index(tile)
    goal_total = find_row(goal_index) + find_column(goal_index)
    state_total = find_row(s.index(tile)) + find_row(s.index(tile))
    result += abs(goal_total - state_total)

  return result

def h_custom(s):
  result = 0
  for tile in s:
    if s.index(tile) != GOAL_STATE.index(tile):
      result += 100

  return result


#<COMMON_DATA>
#</COMMON_DATA>

#<INITIAL_STATE>
# -1 resembles an empty spot
# http://www.theguardian.com/lifeandstyle/2016/apr/28/sudoku-3421-hard
INITIAL_STATE = [[-1 for x in range(9)] for y in range(9)]
INITIAL_STATE[0][1] = 1
INITIAL_STATE[0][4] = 3
INITIAL_STATE[0][7] = 8
INITIAL_STATE[1][0] = 8
INITIAL_STATE[1][2] = 6
INITIAL_STATE[1][6] = 3
INITIAL_STATE[1][8] = 9
INITIAL_STATE[2][2] = 4
INITIAL_STATE[2][3] = 9
INITIAL_STATE[2][7] = 7
INITIAL_STATE[3][2] = 9
INITIAL_STATE[3][4] = 4
INITIAL_STATE[3][5] = 7
INITIAL_STATE[4][5] = 1
INITIAL_STATE[4][8] = 5
INITIAL_STATE[5][2] = 1
INITIAL_STATE[5][6] = 6
INITIAL_STATE[6][1] = 7
INITIAL_STATE[6][3] = 6
INITIAL_STATE[6][5] = 8
INITIAL_STATE[6][6] = 4
INITIAL_STATE[6][7] = 9 
INITIAL_STATE[7][1] = 8
INITIAL_STATE[7][2] = 3
INITIAL_STATE[7][8] = 2
INITIAL_STATE[8][0] = 6
INITIAL_STATE[8][7] = 6

# http://www.sudokukingdom.com/very-easy-sudoku.php
EASY_GAME = [[-1, 7, 2, -1,  -1, 1, 8,  -1, 5],
			 [-1, 5, 1, -1, 3, 7, -1, 9, -1],
			 [4, -1, -1, 2, -1, 8, 1, -1, 7],
			 [-1, 4, 7, 5, 2, -1, 3, -1, -1],
			 [-1, 2, 6, 7, -1, -1, 5, -1, 1],
			 [5, -1, -1, 1, -1, 6, -1, 2, 9],
			 [2, 9, -1, 3, 7, -1, -1, 1, -1],
			 [7, -1, -1, -1, 6, 2, -1, 5, 3],
			 [3, -1, 8, -1, 1, -1, 2, 7, -1]]



CREATE_INITIAL_STATE = lambda: EASY_GAME

#</INITIAL_STATE>

#<OPERATORS>
options = []
temp = copy_state(EASY_GAME)
for x in range(9):
	for y in range(9):
		can_moves = []
		for n in range(1, 10):
			if can_move(temp, n, x, y):
				can_moves.append((n, x, y))	

		if len(can_moves) == 1:
			temp = move(temp, can_moves[0][0], can_moves[0][1], can_moves[0][2])
		else:
			for option in can_moves:
				options.append(option)



OPERATORS = [Operator("Add number " + str(n) + " to row " + str(x) + " and column " + str(y), 
					  lambda s, n=n, x=x,  y=y: can_move(s, n, x, y),			
            	  	  lambda s, n=n, x=x, y=y: move(s, n, x, y))
            for (n, x, y) in options]

#</OPERATORS>

#<GOAL_TEST>
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> 
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<STATE_VIS>
'''
 .  1  . | .  3  . | .  8  . 
 8  .  6 | .  .  . | 3  .  9 
 .  .  4 | 9  .  . | .  7  . 
----------------------------
 .  .  9 | .  4  7 | .  .  . 
 .  .  . | .  .  1 | .  .  5 
 .  .  1 | .  .  . | 6  .  . 
----------------------------
 .  7  . | 6  .  8 | 4  9  . 
 .  8  3 | .  .  . | .  .  2 
 6  .  . | .  .  . | .  6  . 

'''

def render_state(s):
	text = "\n"
	for i in range(len(s)):
		for j in range(len(s[0])):
			if s[i][j] == -1:
				text += " . "
			else:
				text += " " + str(s[i][j]) + " "

			if j == 2 or j == 5: # TO-DO: Avoid hard coding if time
				text += "|"

		text += "\n"
		if i == 2 or i == 5: # TO-DO: Avoid hard coding if time
			text += "----------------------------\n"

	return text
 
#</STATE_VIS>


HEURISTICS = {'h_euclidean': h_euclidean, 'h_hamming':h_hamming,
    'h_manhattan':h_manhattan, 'h_custom':h_custom}
