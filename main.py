import pygame, json, sys, os
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.utils import *

class Main:
    def __init__(self) -> None:
        pygame.init()
        self.load()
        self.screen = pygame.display.set_mode(self.res)
        self.display = pygame.Surface((self.width/2, self.height/2))
        self.clock = pygame.time.Clock()
        self.running = True
        self.movement = [False, False]
        self.assets = {
            'stone': load_images('tiles/stone'),
            'grass': load_images('tiles/grass'),
            'decor': load_images('tiles/decor'),
            'large_decor': load_images('tiles/large_decor'),
            'player': load_image('entities/player.png')
        }
    
    def config(self) -> None:
        self.width, self.height = config["width"], config["height"]
        self.res = config["resolution"]

    def load(self) -> None:
        pygame.display.set_caption("Loading...")
        global config
        if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
            sys.exit("'config.json' not found! Please add it and try again.")
        else:
            with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
                config = json.load(file)
        self.config()
        self.player = PhysicsEntity(self, 'player', (50, 50), (16, 32))
        self.tilemap = Tilemap(self, tilesize=16)

    def update(self) -> None:
        pygame.display.set_caption("Platformer")
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
        pygame.display.update()
        self.clock.tick(60)

    def run(self) -> None: # this function can handle game events in runtime
        while self.running:
            # ingame rendering

            self.display.fill((14, 219, 248))

            self.tilemap.render(self.display)
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            self.update()

            # ingame events

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_SPACE:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                self.load()
    
    def terminate(self) -> None:
        self.running = False
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Main().run()
