import pygame

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}

class Tilemap:
    def __init__(self, game, tilesize=16) -> None:
        self.game = game
        self.tilesize = tilesize
        self.tilemap = {}
        self.tiles_offgrid = []

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap['10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}

    def tiles_near(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tilesize), int(pos[1] // self.tilesize))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles
    
    def physics_rects_near(self, pos):
        rects = []
        for tile in self.tiles_near(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tilesize, tile['pos'][1] * self.tilesize, self.tilesize, self.tilesize))
        return rects

    def render(self, surf):
        for tile in self.tiles_offgrid:
            surf.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])
            
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tilesize, tile['pos'][1] * self.tilesize))