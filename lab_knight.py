import sys

class Board:
	def __init__(self,board=None):
		self.__size = 8
		self.__board = [' '] * self.size() * self.size()

		if board != None :
			if len(board) == len(self.__board):
				self.__board = list(board)
			else:
				raise ValueError('Supplied board is of the wrong size')

	def size(self): 
		return self.__size

	def pretty_print(self):
		''' Print the board to the screen in a nice way'''
		print('_' + '__'*self.size())
		for i in range(0,len(self.__board),self.size()):
			row = self.__board[i:i+self.size()]
			print( '|' + '|'.join(row) + '|' )
		print('‾' + '‾‾'*self.size())

	def __str__(self):
		return ''.join(self.__board)
		
	def set(self,x,y,val):
		''' Put a piece on the board '''
		self.__board[ (y*self.size())+x ] = val
			
	def get(self,x,y):
		''' Get a piece on the board '''
		return self.__board[ (y*self.size())+x ]

def knightify(board):
	# COMPLETE ME, YOU MAY WANT TO WHAT THE BOARD CLASS FUNCTIONS DO FIRST

	#board.pretty_print()
	#board.size()
	#board.get(0,0)
	#board.set(1,1,'x')

	return board

def main():
	tests = [('                  k                                             ',' x x    x   x     k     x   x    x x                            '),
			('k                                                               ','k         x      x                                              '),
			('                                                               k','                                              x      x         k'),
			('                                                                ','                                                                '),
			('                                                         k      ','                                        x x        x     k      '),
			('                                             k                  ','                            x x    x   x     k     x   x    x x '),
			('                  k                          k                  ',' x x    x   x     k     x   x x  x x   x     k     x   x    x x ')]

	errors = 0
	for t, c in tests:
		test = Board(t)

		print('Testing')
		test.pretty_print()

		correctAnswer = Board(c)
		yourAnswer = knightify(test)
		
		if str(correctAnswer) != str(yourAnswer):
			print('Error! expected')
			correctAnswer.pretty_print()

			print('But got')
			yourAnswer.pretty_print()

			errors += 1

		print()

	if errors == 0:
		print('Congratulations, no errors')
	else:
		print('Uh oh, %d error/s remain' % errors)

if __name__ == '__main__':
	sys.exit(main())