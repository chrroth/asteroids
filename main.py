import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, RESPAWN_COOLDOWN_SECONDS
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from lives import LifeIcon

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    lives = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    LifeIcon.containers = (lives, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #asteroid = Asteroid(100, 100, 20)
    asteroidfield = AsteroidField()

    for i in range(1, 4):
            life = LifeIcon(SCREEN_WIDTH - i * 40, SCREEN_HEIGHT - 50)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable.update(dt)

        if player.respawn_cooldown < 0:

            for asteroid in asteroids:        
                if asteroid.collides_with(player):
                    log_event("player_hit")

                    if len(lives.sprites()) == 0:
                            print("Game Over!")
                            sys.exit()
                    else:
                        for life in lives:
                            life.kill()
                            player.respawn()
                            break

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()


        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    
if __name__ == "__main__":
    main()

