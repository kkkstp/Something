import random

class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [['#'] * self.N for i in range(self.N)]
        self.init()

    def init(self):
        a, b = 0, 0
        self.lst_for_position = []

        while len(self.lst_for_position) != self.M:
            a, b = random.randrange(0, self.N), random.randrange(0, self.N)
            if (a, b) not in self.lst_for_position:
                self.lst_for_position.append((a, b))

        for i in range(self.N):
            for j in range(self.N):
                if (i, j) in self.lst_for_position:
                    self.pole[i][j] = Cell(mine=True)
                else:
                    self.pole[i][j] = Cell(mine=False)

        for i, j in self.lst_for_position:

            if i == 0 and j == 0:
                self.pole[i][j + 1].around_mines += 1
                self.pole[i + 1][j + 1].around_mines += 1
                self.pole[i + 1][j].around_mines += 1

            elif i == 0 and j == self.N - 1:
                self.pole[i][j - 1].around_mines += 1
                self.pole[i - 1][j - 1].around_mines += 1
                self.pole[i + 1][j].around_mines += 1

            elif i == self.N - 1 and j == 0:
                self.pole[i][j - 1].around_mines += 1
                self.pole[i - 1][j + 1].around_mines += 1
                self.pole[i][j + 1].around_mines += 1

            elif i == self.N - 1 and j == self.N - 1:
                self.pole[i][j - 1].around_mines += 1
                self.pole[i - 1][j - 1].around_mines += 1
                self.pole[i][j - 1].around_mines += 1

            elif i == 0:
                self.pole[i][j - 1].around_mines += 1
                self.pole[i][j + 1].around_mines += 1
                self.pole[i + 1][j].around_mines += 1
                self.pole[i + 1][j - 1].around_mines += 1
                self.pole[i + 1][j + 1].around_mines += 1

            elif i == self.N - 1:
                self.pole[i][j - 1].around_mines += 1
                self.pole[i][j + 1].around_mines += 1
                self.pole[i - 1][j].around_mines += 1
                self.pole[i - 1][j - 1].around_mines += 1
                self.pole[i - 1][j + 1].around_mines += 1

            elif j == 0:
                self.pole[i - 1][j].around_mines += 1
                self.pole[i + 1][j].around_mines += 1
                self.pole[i][j + 1].around_mines += 1
                self.pole[i - 1][j + 1].around_mines += 1
                self.pole[i + 1][j + 1].around_mines += 1


            elif j == self.N - 1:
                self.pole[i - 1][j].around_mines += 1
                self.pole[i + 1][j].around_mines += 1
                self.pole[i][j - 1].around_mines += 1
                self.pole[i - 1][j - 1].around_mines += 1
                self.pole[i + 1][j - 1].around_mines += 1

            else:
                self.pole[i - 1][j - 1].around_mines += 1
                self.pole[i][j - 1].around_mines += 1
                self.pole[i + 1][j - 1].around_mines += 1
                self.pole[i - 1][j].around_mines += 1
                self.pole[i + 1][j].around_mines += 1
                self.pole[i - 1][j + 1].around_mines += 1
                self.pole[i][j + 1].around_mines += 1
                self.pole[i + 1][j + 1].around_mines += 1

    def show(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.pole[i][j].fl_open == True:
                    print('*', end=' ')
                else:
                    print('#', end=' ')
            print()

    def check(self):
        error_lst = []
        print('Наше поле с минами: \n')
        for i in range(self.N):
            for j in range(self.N):
                if self.pole[i][j].mine == True:
                    print('*', end=' ')
                else:
                    print('#', end=' ')
            print()

        print('Позиции этих мин: ')
        for i in self.lst_for_position:
            print(i, end=' ')
        print('\n')

        for i, j in self.lst_for_position:
            print(f'Для позиции {i, j}:')
            if i == 0 and i == self.N-1 and j == 0 and j == self.N-1:
                continue
            if (self.pole[i-1][j-1].mine) and (self.pole[i][j-1]) and (self.pole[i+1][j-1]) \
                and (self.pole[i-1][j]) and (self.pole[i+1][j]) and (self.pole[i-1][j+1]) \
                and (self.pole[i][j+1]) and (self.pole[i+1][j+1]):
                print('тут всё ок')
            else:
                error_lst.append((i, j))
            input()
        print(error_lst)

pole_game = GamePole(10, 12)