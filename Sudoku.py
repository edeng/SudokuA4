''' Sudoku.py
Luxun Lu & Eden Ghirmai 
CSE415 Spr16 - 4/29/2015
Assignment 4: Problem Formulation
'''

#<METADATA>
PROBLEM_NAME = "Sudoku"
PROBLEM_AUTHORS = ['Eden Ghirmai', 'Luxun Lu']
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

def copy_state(s):
	new = [[-1 for x in range(9)] for y in range(9)]
	for i in len(s):
		for j in len(s):
			new[i][j] = s[i][j]

	return new

def goal_test(s):
	for i in range(len(s)):
		for j in range(len(s)):
			if s[i][j] == -1:
				return False

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


#</COMMON_CODE>

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

CREATE_INITIAL_STATE = lambda: INITIAL_STATE

#</INITIAL_STATE>

#<OPERATORS>
options = []
for x in range(9):
	for y in range(9):
		for n in range(1, 10):
			options.append((n, x, y))

OPERATORS = [Operator("Add number " + str(n) + "to row " + str(x) + " and column " + str(y), 
					  lambda s, n=n, x=x,  y=y: can_move(s, n, x, y),			
            	  	  lambda s, n=n, x=x, y=y: move(s, n, x, y))
            for (n, x, y) in options]

#</OPERATORS>

#<GOAL_TEST>
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> 

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


