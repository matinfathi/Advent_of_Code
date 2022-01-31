import numpy as np


class BingoGame:
    def __init__(self, data):
        self.data = data.astype(int)
        self.marked = np.zeros(self.data.shape).astype(int)
        self.winners = np.zeros(self.data.shape[0]).astype(int)

    def mark(self, num):
        coords = np.where(self.data == num)
        self.marked[coords] = 1

    def mark_winner(self):
        winner_idx = 'None'
        for idx_board, marked_board in enumerate(self.marked):
            if self.winners[idx_board] == 1:
                continue
            for i in range(5):
                win = True
                for j in range(5):
                    if marked_board[i, j] == 0:
                        win = False
                        break
                if win:
                    self.winners[idx_board] = 1
                    winner_idx = idx_board

            for j in range(5):
                win = True
                for i in range(5):
                    if marked_board[i, j] == 0:
                        win = False
                        break
                if win:
                    self.winners[idx_board] = 1
                    winner_idx = idx_board

        return winner_idx

    def score(self, board_idx, called):
        board = self.data[board_idx]
        marked = self.marked[board_idx]
        summation = 0

        for i in range(5):
            for j in range(5):
                if marked[i, j] == 0:
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

for idx, number in enumerate(generated_numbers):
    bingo.mark(number)
    last_winner = bingo.mark_winner()

    if (bingo.winners == 1).all() or idx + 1 == len(generated_numbers):
        score = bingo.score(last_winner, number)
        break

print(score)
