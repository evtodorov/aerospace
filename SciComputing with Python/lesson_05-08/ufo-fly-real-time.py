import pygame as pg

# Initialize pygame module
pg.init()
bgcolor = (63,63,63)  # Set each RGB-value on scale of 0-255

# Load image
print "Loading images"
ufogif   = pg.image.load("UFO.gif")
ufoimg = pg.transform.scale(ufogif, (101,59) )
uforect  = ufoimg.get_rect()

# Create display image name scr
print "Setting up screen"
xmax = 1000
ymax =  600
reso = (xmax,ymax)
scr = pg.display.set_mode(reso)

# Begin position & speed
y  = 0.0  # float y-coordinate: define 100 = whole screen
vy = 40.0 # so 2.5 sec for whole screen

# Start clock: get_ticks is time in milliseconds integer
t0 = float(pg.time.get_ticks())/1000. 

print "Starting game loop"

# loop until end of screen reached
while y<100.:
    pg.event.pump()

# Determine time step
    t = float(pg.time.get_ticks())/1000. 
    dt = t - t0
    t0 = t
    print dt
# Move & draw
    y = y + vy*dt

    xscr = xmax/2
    yscr = ymax - int(y*float(ymax)/100.)
    uforect.center = xscr,yscr

    scr.fill(bgcolor)         # Clear screen
    scr.blit(ufoimg,uforect)   # Blit ufo on scr
    pg.display.flip()          # Frame ready

# Wrap-up
pg.quit()
print "Ready."
