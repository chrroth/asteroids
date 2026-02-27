import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LIFE_SPACING, LIFE_Y_OFFSET
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from lives import LifeIcon
from score import Score

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
    score = Score(SCREEN_WIDTH - 70, SCREEN_HEIGHT - 80)
    AsteroidField()

    for i in range(1, 4):
        LifeIcon(SCREEN_WIDTH - i * LIFE_SPACING, SCREEN_HEIGHT - LIFE_Y_OFFSET)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable.update(dt)

        if player.respawn_cooldown <= 0:

            for asteroid in asteroids:        
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    if not lives:
                        print("Game Over!")
                        return

                    lives.sprites()[-1].kill()
                    player.respawn()          

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    player.update_score()

        for object in drawable:
            object.draw(screen)

        score.draw(screen, player)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()

