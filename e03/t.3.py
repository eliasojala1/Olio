class World:
    def __init__(self, size):
        self.size = size
        self.grid = [[[] for _ in range(size)] for _ in range(size)]

    def add_player(self, player, x, y):
        self.grid[x][y].append(player)
        player.x, player.y = x, y

    def move_player(self, player, x, y):
        self.grid[player.x][player.y].remove(player)
        self.grid[x][y].append(player)
        player.x, player.y = x, y

    def add_item(self, item, x, y):
        self.grid[x][y].append(item)

    def pick_up_item(self, player):
        for obj in self.grid[player.x][player.y]:
            if isinstance(obj, Item):
                player.inventory.append(obj)
                self.grid[player.x][player.y].remove(obj)
                break

    def __str__(self):
        return "\n".join(" ".join("P" if any(isinstance(obj, Player) for obj in cell) else 
                                  "I" if any(isinstance(obj, Item) for obj in cell) else "." for cell in row)
                         for row in self.grid)


class Player:
    def __init__(self, name):
        self.name = name
        self.x = None
        self.y = None
        self.inventory = []


class Item:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    world = World(5)
    p1 = Player("Rock")
    i1 = Item("Axe")

    world.add_player(p1, 2, 2)
    world.add_item(i1, 2, 2)

    print(world)

    world.pick_up_item(p1)
    world.move_player(p1, 3, 3)

    print(world)