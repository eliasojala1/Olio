class World:
    def __init__(self, size):
        self.grid = [[None] * size for _ in range(size)]
        self.players = []

    def add_player(self, player, x, y):
        if self.grid[x][y] is None:
            self.grid[x][y] = player
            self.players.append(player)

    def move_player(self, player, x, y):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == player:
                    self.grid[i][j] = None
                    self.grid[x][y] = player
                    return

    def __str__(self):
        return "\n".join(" ".join("P" if p else "." for p in row) for row in self.grid)

class Player:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    p = Player("Rock")
    w = World(5)
    
    w.add_player(p, 2, 2)
    print(w)

    w.move_player(p, 3, 3)
    print(w)