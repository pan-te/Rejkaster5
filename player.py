import pygame
import math

class Player:
	def __init__(self,posx,posy,dir,speed,fov):
		self.posx = posx+0.5
		self.posy = posy+0.5
		self.dir = dir
		self.speed = speed
		self.fov = fov
	def controls(self,keys,map):
		if keys[pygame.K_a]: self.dir-=5
		if keys[pygame.K_d]: self.dir+=5
		if keys[pygame.K_w]:
			if map[math.trunc(self.posx+self.speed*math.cos(math.radians(self.dir)))][math.trunc(self.posy)]==0:
				self.posx+=self.speed*math.cos(math.radians(self.dir))
			if map[math.trunc(self.posx)][math.trunc(self.posy+self.speed*math.sin(math.radians(self.dir)))]==0:
				self.posy+=self.speed*math.sin(math.radians(self.dir))
		if keys[pygame.K_s]:
			if map[math.trunc(self.posx-self.speed*math.cos(math.radians(self.dir)))][math.trunc(self.posy)]==0:
				self.posx-=self.speed*math.cos(math.radians(self.dir))
			if map[math.trunc(self.posx)][math.trunc(self.posy-self.speed*math.sin(math.radians(self.dir)))]==0:
				self.posy-=self.speed*math.sin(math.radians(self.dir))
		if keys[pygame.K_ESCAPE]:
			exit()