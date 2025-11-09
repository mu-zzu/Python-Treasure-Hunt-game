import pygame
import random
import sys

pygame.init()
width,height=600
grid_size=5
cell_size=grid_size//width

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen=pygame.display.set_mode((width,height))
pygame.display.setcaption("Treasure Hunt")
treasure_x=random.randint(0,grid_size-1)
treasure_y=random.randint(0,grid_size-1)
guesses = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
attempts = 0
max_attempts = 5
font = pygame.font.Font(None, 36)
game_over = False
game_status = ""
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))
def display_message(message, color, y_offset=0):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text, text_rect)
def main()
 golba; gameover,attempts,game_status
  clock=pygame.time.Clock()
while True:
  screen.fill(WHITE)
  draw_grid()
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
     pygame.quit()
     sys.exit()
    if event.type==pygame.MOUSEBUTTONDOWN and not game_over:
     mouse_x,mouse_y=event.pos
     grid_x=mouse_x//CELL_SIZE
     grid_y=mouse_y//CELL_SIZE
     if not guesses[grid_y][grid_x]:
      guesses[grid_y][grid_x]=True
      attempts+=1
        if(grid_x,grid_y)==(tresure_x,treasure_y):
         game_over=True
         game_status="won"
        elif attempts>=max_attempts:
         game_over=True
         game_status="lost"
         for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if guesses[y][x]:
                    if (x, y) == (treasure_x, treasure_y):
                        pygame.draw.rect(screen, GREEN, rect)
                    else:
                        pygame.draw.rect(screen, RED, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)
            if game_over:
            if game_status == "won":
                display_message("You Found the Treasure!", BLUE)
            elif game_status == "lost":
                display_message("You Lost the Game!", RED)
        else:
            display_message("Click to Hunt for Treasure", BLACK, y_offset=-200)
            display_message(f"Attempts Left: {max_attempts - attempts}", BLACK, y_offset=-150)
            print(hello)
        pygame.display.flip()
        clock.tick(30)
         
     
     


