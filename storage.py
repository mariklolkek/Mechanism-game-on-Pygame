import pygame as p,time as t,random as r,numba as nb,taichi as ti, numpy as n
p.init()

# Pygame
display_w,display_h = 1200,700
dis_w,dis_h = display_w,display_h
Clock = clock = p.time.Clock()
cords = [0,0]
key = p.key.get_pressed()

f = 0

#F3
F3 = True
pause = False

#where
where = "menu"


mx,my = 0,0

# choose
choosen_block = 0
blocks = ["rl","rr","ru","rd",
		   "pl","pr","pu","pd",
		   "block",
		   "sl","sr","su","sd",
		   "gl","gr","gu","gd","ga","en",
		   "agl","agr","agu","agd","aga",
		   "du","dr","du","dd",
		   " ","robot"
		   ]

blocks_images = []
print(len(blocks))
max_blocks = len(blocks)-1
#"l.png","r.png","u.png","d.png",


features = ["delete_all",
			"plus_size",
			"minus_size",
			"",
			"",
			]

tick = False


current_size = (display_w,display_h)
FPS = 120

#colors
red   = (255,0,0)
blue  = (0,0,255)
green = (0,255,0)
white = (255,255,255)
black_c = (0,0,0)

fonts = []


arena = []
size = 25*2


for i in nb.prange(round((display_w/size)*(display_h/size))):
	arena.append("[ ]")
	#arena.append("["+r.choice(blocks)+"]")

'''arena[round(8*(display_w/size))] = "[pd]"
arena[round(9*(display_w/size))] = "[#]"
arena[round(10*(display_w/size))] = "[#]"'''
#for i in nb.prange(round(display_h/size)):
	#arena[round(i*(display_w/size))+11] = "[rl]"
#for i in nb.prange(round(display_w/size)):
	#arena[round(i*(display_h/size))] = "[rd]"











'''
[0] ничего 1 		+
[p] поршень 4 		+
[r] двигающийся 4 	+
[#] блок 1 			+
[s] спавнер 4 		-
[g] провод 5 		-
[d] уничтожитель 4	-
[n] наблюдатель 4	-
[q] поворачиватель 1-
[ ] 
[ ] 
[ ] 
[ ] 
[ ] 
[ ] 
[ ] 
[ ] 
[ ] 
[ ] 
[ ] 











'''