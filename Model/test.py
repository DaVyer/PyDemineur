class Quoridor:
    def __init__(self, players):
        self.players = players
        self.board = [['.' for i in range(9)] for j in range(9)]
        self.positions = {players[0]: (0, 4), players[1]: (8, 4)}

    def move(self, player, direction):
        x, y = self.positions[player]
        if direction == 'U':
            x -= 1
        elif direction == 'D':
            x += 1
        elif direction == 'L':
            y -= 1
        elif direction == 'R':
            y += 1
        self.positions[player] = (x, y)
        self.board[x][y] = player[0]

    def display(self):
        print("  ", end="")
        print(" ".join([str(i) for i in range(1, 9)]))
        for i in range(9):
            print(i+1, end=" ")
            print(" ".join(self.board[i]))

if __name__ == '__main__':
    game = Quoridor(['P1', 'P2'])
    while True:
        game.display()
        player = game.players[0]
        move = input(f"{player}, make your move (U, D, L, R): ")
        game.move(player, move)
        game.players = game.players[::-1]
