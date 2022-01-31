import numpy as np


class BingoGame:
    def __init__(self, data):
        self.data = data.astype(int)
        self.marked = np.zeros(self.data.shape).astype(int)

    def mark(self, num):
        coords = np.where(self.data == num)
        self.marked[coords] = 1

    def search_winner(self):
        for idx, marked_board in enumerate(self.marked):
            for i in range(5):
                win = True
                for j in range(5):
                    if marked_board[i, j] == 0:
                        win = False
                if win:
                    return idx

            for j in range(5):
                win = True
                for i in range(5):
                    if marked_board[i, j] == 0:
                        win = False
                if win:
                    return idx

        return False

    def score(self, idx, called):
        board = self.data[idx]
        marked_board = self.marked[idx]
        summation = 0

        for i in range(5):
            for j in range(5):
                if marked_board[i, j] == 0:
                    summation += board[i, j]

        return summation * called


input_path = './input_day4'

with open(input_path, 'r') as f:
    data = f.read().split('\n\n')

generated_numbers = list(map(int, data[0].split(',')))
boards = np.array(
    [np.array(list(map(int, board.replace('\n', ' ').strip().split()))).reshape(5, 5) for board in data[1:]])

bingo = BingoGame(boards)

score = 0

for number in generated_numbers:
    bingo.mark(number)
    result = bingo.search_winner()
    if result != False:
        score = bingo.score(result, number)
        break

print(score)
