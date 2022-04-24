import pygame
running = True
#Määrab värvid mida kasutada
VALGE = (255, 255, 255)
PUNANE = (255, 0, 0)
KOLLANE = (255, 255, 0)
ROHELINE = (0, 255, 0)
#Joonistab akna suuruses 300x300
screen=pygame.display.set_mode([300,300])
#Määrab akna nime
pygame.display.set_caption("Valgusfoor - Laura Kramp")
#määrab taustavärvi
screen.fill([0, 0, 0])
#Joonistab valgusfoori ristküliku
pygame.draw.rect(screen, VALGE, [76, 17, 140, 265], 2)


#defineerib valgusfooride ringid ja värvid
def draw_valgusfoor(screen, x, y):
    pygame.draw.circle(screen, PUNANE, [60 + x, 7 + y], 37)
    pygame.draw.circle(screen, KOLLANE, [60 + x, 84 + y], 37)
    pygame.draw.circle(screen, ROHELINE, [60 + x, 163+ + y], 37)
draw_valgusfoor(screen,85,65)
pygame.display.flip()

#võimaldab akna lahti hoida ja sulgeda ristist
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False