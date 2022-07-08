#!/usr/bin/env python3

try:
	from swampy.TurtleWorld import *
except ImportError:
	from TurtleWorld import *
	
	
def koch(t,num,n):
	if num == 0:
		t.fd(n)
	else:
		koch(t,num-1,n/3)
		t.rt(85)
		koch(t,num-1,n/3)
		t.lt(170)
		koch(t,num-1,n/3)
		t.rt(85)
		koch(t,num-1,n/3)
	
	
def Cesàro_fractal(t,num,n):
	for i in range(5):
		koch(t, num, n)
		t.rt(72)
		
		
world = TurtleWorld()
bob = Turtle()
bob.delay = 0#绘画延迟
bob.x = 0
bob.y = 160
bob.redraw()#取消绘制，然后重新绘制动物
bob.rt(36)
Cesàro_fractal(bob,5,1000)
bob.y = -10
bob.heading = 90
bob.redraw()
world.mainloop()
