# tic_tac_toe.py


class Player:
    def __init__(self, name=None, token=None):
        self.name = name
        self.token = token

    def __repr__(self):
        return f'{self.name} is {self.token}'


class Game:
    def __init__(self):
        self.board = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]

    def __repr__(self):
        ret = ''
        for l in self.board:
            ret += str(l) + '\n'
        return ret

    def move(self, x, y, player):

        self.board[y][x] = player.token
        return self.board

    def calc_winner(self):
        loop = False
        while loop:
            if self.board[0][0] == self.board[0][1] == self.board[0][2]:
                # loop = True
                print('Winner')
            else:

                print('No winner yet..')


p1 = Player('player_1', 'X')
p2 = Player('player_2', 'O')

print(p1)
print(p2)

board = Game()
print(board)
board.move(0, 0, p1)
print(board)
board.move(1, 1, p2)
print(type(board.calc_winner()))
