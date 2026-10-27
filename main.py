import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	#INITIALIZE PYTHON GAME AND SET UP THE GAME WINDOW
	
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	#CREATE THE CLOCK OBJECT AND INITIALIZE DT

	clock =	pygame.time.Clock()
	dt = 0.0

	#INSTANTIATE THE PLAYER IN THE CENTER OF THE SCREEN
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


	#Main Game Loop
	while True:
		log_state()

		#HANDLE USER EVENTS(LIKE CLICKING THE WINDOW CLOSE BUTTON)

		for event in pygame.event.get():
   			if event.type == pygame.QUIT:
       				return
		#UPDATE GAME OBJECTS
		
		player.update(dt)
		
		#RENDER STEP : FILL SCREEN BLACK, DRAW THE PLAYER, AND REFRESH DISPLAY

		screen.fill("black")
		player.draw(screen)
		pygame.display.flip()
		
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
