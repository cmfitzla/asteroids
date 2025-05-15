import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	# Main game loop
	running = True
	while running:
		# Calculate delta time
		dt = clock.tick(60) / 1000 # Convert milliseconds to seconds

		# Handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# Update game state
		updatable.update(dt)

		for asteroid in asteroids:
			if player.collisions(asteroid):
				print(f"Game Over!")
				sys.exit()
			
		# Render/draw everything	   
		screen.fill((0,0,0))
		for sprite in drawable:
			sprite.draw(screen)
		# ...other drawing code...

		pygame.display.flip()

    


if __name__ == "__main__":
	main()
