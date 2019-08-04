import pygame
import math
import sys
import player

print("Rejkaster Engine V\nv0.1a\n(c)by Daniel Sadlik (pan-te)\nsadlikd@gmail.com")

size = []
if len(sys.argv)==3:
	size = [int(sys.argv[1]),int(sys.argv[2])]
else: size = [1024,768]

map = [
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,1,1,0,0,0,0,0,0,0,0,0,3,0,1],
	[1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
	[1,0,1,0,9,1,0,0,0,0,0,0,0,2,0,1],
	[1,0,0,0,0,0,2,3,6,7,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,7,0,0,0,2,0,1],
	[1,0,0,0,0,0,3,0,0,6,0,1,0,0,0,1],
	[1,0,1,0,0,0,4,0,0,5,0,1,0,3,0,1],
	[1,0,2,0,0,0,5,0,0,5,0,0,0,0,0,1],
	[1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

palette = [
	[1,0.5,0],
	[0.5,1,0],
	[1,0,0.5],
	[0.5,0,0],
	[0,0.3,0],
	[0,0,0.6],
	[1,1,0.5]
]

background = pygame.transform.scale(pygame.image.load("back.png"), size)

pygame.init()
window = pygame.display.set_mode(size)
pygame.display.set_caption("Rejkaster Engine V v0.1a")
ray_pos = 0
ray_range = 6
gracz = 0
running = True
klok = pygame.time.Clock()
#search for a player
for row in range(len(map)):
	if (9 in map[row]):
		#print("Start pos:",row,map[row].index(9))
		gracz = player.Player(map[row].index(9),row,0,0.125,60)
		map[map[row].index(9)][row] = 0
half_fov = gracz.fov/2
half_height = math.trunc(size[1]/2)
draw_step = math.trunc(size[0]/gracz.fov)
draw_const = half_height*90/gracz.fov
color = []
#main loop
while(running):
	window.blit(background,(0,0))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running = False
	keys = pygame.key.get_pressed()
	gracz.controls(keys,map)
	for deg in range(gracz.fov):
		l = 0.1
		while (l < ray_range):
			ray_pos = [gracz.posx+math.cos(math.radians(gracz.dir-half_fov+deg))*l,gracz.posy+math.sin(math.radians(gracz.dir-half_fov+deg))*l]
			ray_pos = [math.trunc(ray_pos[0]),math.trunc(ray_pos[1])]
			if (map[ray_pos[0]][ray_pos[1]]!=0)&(map[ray_pos[0]][ray_pos[1]]!=9):
				rectx = draw_step*(deg)
				recty = half_height - draw_const/(l*math.cos(math.radians(deg-half_fov)))
				recth = size[1]-2*recty
				color = [255*(1-l/ray_range)*palette[(map[ray_pos[0]][ray_pos[1]])-1][0],255*(1-l/ray_range)*palette[(map[ray_pos[0]][ray_pos[1]])-1][1],255*(1-l/ray_range)*palette[(map[ray_pos[0]][ray_pos[1]])-1][2]]
				pygame.draw.rect(window,color,pygame.Rect(rectx,recty,draw_step,recth))
				break
			l+=0.1
	pygame.display.update()
	klok.tick(30)
	
	
