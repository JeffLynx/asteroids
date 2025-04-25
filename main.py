import sys
import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
	pygame.init()	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	
	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatables, drawables)
	Asteroid.containers = (asteroids, updatables, drawables)
	AsteroidField.containers = updatables
	Shot.containers = (shots, updatables, drawables)
	asteroid_field = AsteroidField()
	

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	
	dt = 0	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updatables.update(dt)

		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()
			for shot in shots:
				if asteroid.collides_with(shot):
					shot.kill()
					asteroid.split()
	
		screen.fill("black")

		for drawable in drawables:
			drawable.draw(screen)
	
		pygame.display.flip()

		dt = clock.tick(60) / 1000
		
if __name__ == "__main__":
	main()
