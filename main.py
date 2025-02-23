import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    dt: float = 0
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)

        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        passed = clock.tick(60)
        dt = passed / 1000

if __name__ == "__main__":
    main()
