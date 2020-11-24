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

print "Starting for-loop"

# loop until end of screen reached
for i in range(500):
    pg.event.pump()


# Move & draw
    y = ymax+float(i)/100.*ymax

    xscr = xmax/2
    yscr = ymax-int(float(i)/500.*ymax)
    uforect.center = xscr,yscr

    scr.fill(bgcolor)         # Clear screen
    scr.blit(ufoimg,uforect)   # Blit ufo on scr
    pg.display.flip()          # Frame ready

# Wrap-up
pg.quit()
print "Ready."
