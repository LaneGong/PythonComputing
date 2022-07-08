"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *
#异常处理

def square(t, length):#画正方形，长度为length
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        fd(t, length)
        lt(t)


def polyline(t, n, length, angle):#多边线，接口为对象，边数，长度，边与边之间的角度
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):#多边形，接口为对象，边数，长度
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n #计算边与边之间的角度
    polyline(t, n, length, angle) #调用polyline函数


def arc(t, r, angle): #画圆弧，接口为对象，圆半径，圆周角
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360 #弧长
    n = int(arc_length / 4) + 1 #利用n边形近似圆弧
    step_length = arc_length / n #每个短边的长度
    step_angle = float(angle) / n #边与边之间的角度

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2) 
    polyline(t, n, step_length, step_angle) #调用polyline
    rt(t, step_angle/2)


def circle(t, r): #调用arc画圆
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360) #圆周角为360，即圆


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001
    # draw a circle centered on the origin
    #radius = 100 #半径
    while True:
        #pu(bob)
        #fd(bob, radius)
        #lt(bob)
        #pd(bob)
        print('以下为测试各个函数：')
        print('1. square函数')
        print('2. polyline函数')
        print('3. polygon函数')
        print('4. arc函数')
        print('5. circle函数')
        print('0. 退出')
        choice=int(input('请输入：'))
        if choice==0:
            break
        elif choice==1:
            world.clear()
            length=int(input('请输入正方形边长：'))
            square(bob,length)
        elif choice==2:
            world.clear()
            length=int(input('请输入多边线边长：'))
            num=int(input('请输入多边线边数：'))
            angle=int(input('请输入边与边之间的角度：'))
            polyline(bob,num,length,angle)
        elif choice==3:
            world.clear()
            num=int(input('请输入多边形边数：'))
            length=int(input('请输入多边形边长：'))
            polygon(bob,num,length)
        elif choice==4:
            world.clear()
            radius=int(input('请输入半径：'))
            angle=int(input('请输入圆周角读数：'))
            arc(bob,radius,angle)
        else:
            world.clear()
            radius=int(input('请输入半径：'))
            circle(bob, radius)

    