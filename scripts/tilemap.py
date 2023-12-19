class Tilemap:
    def __init__(self, tilesize=16) -> None:
        self.tilesize = tilesize
        self.tilemap = {}
        self.tiles_offgrid = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}
