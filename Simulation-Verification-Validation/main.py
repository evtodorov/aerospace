# -*- coding: utf-8 -*-
"""
This file contains the top level architecture of the numerical solver

@revision: 1
@author: etodorov
@dat: 14 Feb 16
"""

from base import Problem
import solversImports as solvers
Boeing777 = Problem()

# Procedural execution of each of the units
# rm everything below this line and reuse auto.py

#statics
solvers.statics.check_input(Boeing777)
solvers.statics.solve(Boeing777)
solvers.statics.check_output(Boeing777)
#sfd
solvers.sfd.check_input(Boeing777)
solvers.sfd.solve(Boeing777)
solvers.sfd.check_output(Boeing777)
#bmd
solvers.bmd.check_input(Boeing777)
solvers.bmd.solve(Boeing777)
solvers.bmd.check_output(Boeing777)
#tmd
solvers.tmd.check_input(Boeing777)
solvers.tmd.solve(Boeing777)
solvers.tmd.check_output(Boeing777)
#discretize
solvers.discretize.check_input(Boeing777)
solvers.discretize.solve(Boeing777)
solvers.discretize.check_output(Boeing777)
#sectionProps
solvers.sectionProps.check_input(Boeing777)
solvers.sectionProps.solve(Boeing777)
solvers.sectionProps.check_output(Boeing777)
#sigma
solvers.sigma.check_input(Boeing777)
solvers.sigma.solve(Boeing777)
solvers.sigma.check_output(Boeing777)
#shearFlow
solvers.shearFlow.check_input(Boeing777)
solvers.shearFlow.solve(Boeing777)
solvers.shearFlow.check_output(Boeing777)
#qtorsion
solvers.qtorsion.check_input(Boeing777)
solvers.qtorsion.solve(Boeing777)
solvers.qtorsion.check_output(Boeing777)
#shearStress
solvers.shearStress.check_input(Boeing777)
solvers.shearStress.solve(Boeing777)
solvers.shearStress.check_output(Boeing777)
#frameShear
solvers.frameShear.check_input(Boeing777)
solvers.frameShear.solve(Boeing777)
solvers.frameShear.check_output(Boeing777)
#mohr
solvers.mohr.check_input(Boeing777)
solvers.mohr.solve(Boeing777)
solvers.mohr.check_output(Boeing777)

print "SOLVED"
#some visualization
import matplotlib.pyplot as plt
import numpy as np
o = Boeing777

Y = o.vonMisesStress_ring/1e+6 #to MPA
idY = np.unravel_index(Y.argmax(),Y.shape)

print "Max stress", Y.max(), "MPa @ z = ", o.z[idY[0]], ", (x,y) = ", o.xr[idY[1]], o.yr[idY[1]] 
z = o.z


theta = np.arctan2(o.yr,o.xr)
idRoll = np.argmax(theta > 0)
Yrolled = np.roll(Y, -idRoll, axis=1)
taurolled = np.roll(o.tau_totr, -idRoll, axis=1)/1e+6
sigmarolled = np.roll(o.sigma_z_r, -idRoll, axis=1)/1e+6
q_frame1 = np.roll(o.q_frame1, -idRoll)
q_frame2 = np.roll(o.q_frame2, -idRoll)

plt.figure()

plt.subplot(231)
plt.xlabel("Theta (Deg)")
plt.ylabel("z-Position (m)")
plt.imshow(Yrolled, extent=[0,360,z[0],z[-1]], aspect = 7)
plt.colorbar()
plt.title("Von Mises stress ring")

plt.subplot(232)
plt.xlabel("Theta (deg)")
plt.ylabel("z-Position (m)")
plt.imshow(sigmarolled, extent=[0,360,z[0],z[-1]], aspect = 7)
plt.title("Total normal stress ring")
plt.colorbar()

plt.subplot(233)
plt.xlabel("Theta (deg)")
plt.ylabel("z-Position (m)")
plt.imshow(taurolled, extent=[0,360,z[0],z[-1]], aspect = 7)
plt.title("Total shear stress ring")
plt.colorbar()

plt.subplot(234)
plt.xlabel("x-position (m)")
plt.ylabel("z-Position (m)")
plt.imshow(o.vonMisesStress_floor, extent=[-o.Lfloor,o.Lfloor,z[0],z[-1]], aspect=0.1)
plt.title("Von Mises stress floor")
plt.colorbar()

plt.subplot(235)
plt.imshow(o.sigma_z_f, extent=[-o.Lfloor,o.Lfloor,z[0],z[-1]], aspect=0.1)
plt.xlabel("x-position (m)")
plt.ylabel("z-Position (m)")
plt.title("Total normal stress floor")
plt.colorbar()

plt.subplot(236)
plt.xlabel("x-position (m)")
plt.ylabel("z-Position (m)")
plt.imshow(o.tau_totf, extent=[-o.Lfloor,o.Lfloor,z[0],z[-1]], aspect=0.1)
plt.title("Total shear stress floor")
plt.colorbar()
#plt.show()


data1=np.genfromtxt("validation.rpt",skip_header=15,skip_footer=25341-9690,usecols = (2,3,4,5))
data2=np.genfromtxt("validation.rpt",skip_header=12674,skip_footer=25341-22349,usecols = (5))

xx = data1[:,0]
yy = data1[:,1]
zz = -data1[:,2]
Yobserved = (data1[:,3]+data2)/2
idz = np.argsort(zz)

xx = xx[idz]
yy = yy[idz]
zz = zz[idz]
Yobserved = Yobserved[idz]
tt = np.arctan2(yy,xx)
tt = np.array([x if x >= 0 else 2*np.pi + x for x in tt])

for i in xrange(len(zz)/52):
    ii = i*52
    iii = (i+1)*52
    idt = np.argsort(tt[ii:iii])
    tt[ii:iii] = (tt[ii:iii])[idt]
    zz[ii:iii] = (zz[ii:iii])[idt]
    Yobserved[ii:iii] = (Yobserved[ii:iii])[idt]

Yobserved = np.reshape(Yobserved,(len(zz)/52,52))

floor1=np.genfromtxt("validation.rpt",skip_header=9687,skip_footer=25341-12666,usecols = (2,3,4,5))
floor2=np.genfromtxt("validation.rpt",skip_header=22346,skip_footer=16,usecols = (5))

xxf = floor1[:,0]
zzf = -floor1[:,2]
Y_floor_observed = (floor1[:,3]+floor2)/2
idzf = np.argsort(zzf)
xxf = xxf[idzf]
Y_floor_observed = Y_floor_observed[idzf]

for i in xrange(len(zzf)/16):
    ii = i*16
    iii = (i+1)*16
    idxxf = np.argsort(xxf[ii:iii])
    xxf[ii:iii] = (xxf[ii:iii])[idxxf]
    zzf[ii:iii] = (zzf[ii:iii])[idxxf]
    Y_floor_observed[ii:iii] = (Y_floor_observed[ii:iii])[idxxf]

Y_floor_observed = np.reshape(Y_floor_observed,(len(zzf)/16,16))

plt.figure()
plt.subplot(121)
plt.xlabel("Theta (deg)")
plt.ylabel("z-Position on ring")
plt.imshow(Yrolled, extent=[0,360,z[0],z[-1]], aspect = 7)
plt.title("Von Mises stress ring computed")
plt.colorbar()

plt.subplot(122)
plt.xlabel("Theta (deg)")
plt.ylabel("z-Position on ring")
plt.imshow(Yobserved, extent=[0,360,z[0],z[-1]], aspect = 7)
plt.title("Von Mises stress ring observed")
plt.colorbar()
#plt.show()

plt.figure()
plt.subplot(121)
plt.xlabel("x-Position on floor (m)")
plt.ylabel("z-Position on floor (m)")
plt.imshow(np.sqrt(o.sigma_z_f**2 + 3*o.tau_totf**2)/1e+6, extent=[-o.Lfloor,o.Lfloor,z[0],z[-1]], aspect = 1./3)
plt.title("Von Mises stress floor computed")
plt.colorbar()

plt.subplot(122)
plt.xlabel("x-Position on floor (m)")
plt.ylabel("z-Position on floor (m)")
plt.imshow(Y_floor_observed, extent=[-o.Lfloor,o.Lfloor,z[0],z[-1]], aspect = 1./3)
plt.title("Von Mises stress floor observed")
plt.colorbar()

plt.figure()
plt.subplot(221)
plt.xlabel("z-position (m)")
plt.ylabel("Shear force (N)")
o.Vx_vec = np.vectorize(o.Vx)
plt.plot(o.z, o.Vx_vec(o.z))
plt.title("Shear in x")

plt.subplot(222)
plt.xlabel("z-position (m)")
plt.ylabel("Shear force (N)")
o.Vy_vec = np.vectorize(o.Vy)
plt.plot(o.z, o.Vy_vec(o.z))
plt.title("Shear in y")

plt.subplot(224)
plt.xlabel("z-position (m)")
plt.ylabel("Moment (Nm)")
o.Mx_vec = np.vectorize(o.Mx)
plt.plot(o.z, o.Mx_vec(o.z))
plt.title("Moment around x")

plt.subplot(223)
plt.xlabel("z-position (m)")
plt.ylabel("Moment (Nm)")
o.My_vec = np.vectorize(o.My)
plt.plot(o.z, o.My_vec(o.z))
plt.title("Moment around y")

plt.figure()
plt.subplot(121)
plt.xlabel("Theta (deg)")
plt.ylabel("Shear flow (N/m)")
plt.plot(np.degrees(theta), q_frame1)
plt.title("Shear flow in frame 1")

plt.subplot(122)
plt.xlabel("Theta (deg)")
plt.ylabel("Shear flow (N/m)")
plt.plot(np.degrees(theta), q_frame2)
plt.title("Shear flow in frame 2")


plt.show()
