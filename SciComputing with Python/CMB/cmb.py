# -*- coding: utf-8 -*-
"""
Created June 2014

@author: etodorov
"""
from load import *
pg.init()

game = Game()
Matter.image = Matter.image.convert_alpha()
t0 = game.start
loops = 0

while game.running:
    loops += 1

    pg.event.pump()
    t = pg.time.get_ticks()*0.001
    dt = t - t0
    t0 = t
    #print dt
    #check if quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game.end()
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        game.running = False       
    
    #calculate the forces between the cells (bruteforce patricleVparticle)
    for cell in cells:
        cell.Fx = 0 
        cell.Fy = 0
        for other in cells:
            if(cell!=other): cell.attract(other)
     
        cell.newton(dt)
    
    #calculate the forces in the cell (barycentric approximation)
    #reset the forces
    Fx *= 0.
    Fy *= 0.
    i=0
    bcX = x.copy()
    bcY = y.copy()
    bcM = m.copy()

    for cell in cells:
        #check which body is in the cell
        boolR =np.floor(y/cell.h) == cell.row
        boolC = np.floor(x/cell.w) == cell.col
        aBool =  boolR * boolC  #and
        #barycenter location
        cell.barycenter(m[aBool],x[aBool],y[aBool])         
        bcX[aBool]=cell.x
        bcY[aBool]=cell.y
        bcM[aBool]=cell.m
        Fx[aBool]=cell.Fx/max(len(aBool[aBool]),1)
        Fy[aBool]=cell.Fy/max(len(aBool[aBool]),1)
    
    #calculate the forces in the cells    
    Fx,Fy = gravityVec(m,x,y,Fx,Fy,bcX,bcY,bcM)
     
    #particle positions
    x,y,vx,vy,ax,ay,Fx,Fy = newtonVec(x,y,vx,vy,ax,ay,Fx,Fy,m,dt)

    #prepare the bodies for drawing
    for X,Y,body in zip(x,y,bodies):
        body.update(X,Y)
        
    #draw everything
    game.screen.fill((0,0,0))   
    bodies.draw(game.screen)
    
    if(not loops%100): print "fps:",1/dt    #print fps
    pg.event.pump()
    pg.display.flip()
pg.quit()   
