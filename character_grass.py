from pico2d import *
import math
open_canvas()

# fill here
grass =load_image('grass.png')
character = load_image('character.png')
grass.draw_now(400,30)
x,y=400,90
time_=0
check=True
check0=True
check1=False
temp=+1
while(time_<5000):
    time_+=1
    if(check0):
        if(x==400 and y==90):
            if(check1):
                check0=False
                check1=False
            else:
                check1=True
        delay(0.0005)
        if(check):
            x+=temp*2
            clear_canvas()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            if(not(x==780 or x==20)):
                continue
            elif(x==780):
                check=False
                temp=1
            elif(x==20):
                check=False
                temp=-1
        else:
            y+=temp*2
            clear_canvas()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            if(not(y==600 or y==90)):
                continue
            elif(y==600):
                check=True
                temp=-1
            elif(y==90):
                check=True
                temp=1
    else:
        for i in range(0,361):
            clear_canvas()
            grass.draw_now(400,30)
            x,y=400+200*math.sin(2*i/360*math.pi),290-200*math.cos(2*i/360*math.pi)
            character.draw_now(x,y)
            delay(0.001)
        check0=True
#
close_canvas()
