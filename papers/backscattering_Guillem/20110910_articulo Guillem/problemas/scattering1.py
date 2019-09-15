from math import sqrt, pi, log10,e
from numpy import exp

#give an output filename is you wish to do so
import sys
try:
   filename = sys.argv[1]
except IndexError:
   filename = 'datos.dat'

"""
D**2 corresponds to the output intensity of the ring. A lossless ring should
have normalized output equal to one always.

La matriz que resulta del producto es la matriz de transferencia pero nosotros
hemos resuelto el problema con la matriz de scattering. Queremos:
                    (B,b)=T(C,c) -> (C,b)S(c,B)

( r   t  )
( t'  r' )

"""

"""
All distances and wavelengths are assumed to be in micrometers. Angles in
radians

========================Physical Constats====================================
          k: Coupling of ring and waveguide
     radius: Radius of the resonator
      theta: Position of first scattering event
delta_theta: Angular distance to second scattering event. Check that theta +
             delta_theta < 2pi or expect the worst
         r1: Reflectivity of first scattering point
         r2: Reflectivity of second scattering point
       alfa: Losses in the ring
=============================================================================

========================Simulation Parameters================================
lamb_ini: Initial value of lambda
lamb_end: Final value of lambda
    step: Size of the simulation step
=============================================================================
"""
####PHYSICAL CONSTANTS#####
K = 0.0534
radius = 15.
R = 0.001
neff = 3.5

T = 1. - R

alfa = 14.45  #dB/cm
alfa /= 4.34294482
alfa *= 10**(-4.)

m = sqrt(1.- K)    #The other part to k
r = sqrt(R)
t = sqrt(T)

L = 2.*pi*radius
a = exp(-1.*alfa*L)

z = radius * pi * .345
zp = L - z
delta = zp - z

####SIMULATION PARAMETERS####
lamb_ini = 1.4030
lamb_end = 1.4045
step = 0.000001


#Open output file
outfile = open(filename, 'w')
outfile.write(('#radius =%.3f; K=%.3f; R=%.4f; alfa=%.4f\n')%(radius,K,R,alfa))


lamb = lamb_ini
while lamb < lamb_end:
   n = neff + 1j*alfa*lamb/(4.*pi)
   k = 2.*pi*n/lamb

   x = exp(1j*k*L)
   x_ = 1./x
   xd = exp(1j*k*delta)
   xd_ = 1./xd

   T11 =x *(a/t)
   T22 =x_ *(a/t)
   T12 =-r*xd *(a/t)
   T21 =-r*xd_ *(a/t)

   T = [[T11,T12],[T21,T22]]

   #T -> S
   S11 = T[0][1]/T[1][1]
   S12 = (T[0][0]*T[1][1] - T[0][1]*T[1][0])/T[1][1]
   S21 = 1./T[1][1]
   S22 = -T[1][0]/T[1][1]

   aux1 = 1. - m*S12 #auxiliary variable to make next expression cleaner
   aux2 = 1. - m*S21
   rr = S11*S22
   
   C = ((S12*aux2) + m*rr)/((aux1*aux2)-m*m*rr)
   D = abs(m - K*C)**2     #Through-port
   #B = 1j*k + m*C
   #a = abs(B*1j*k*S22*(1. + S12*m/aux1))**2  #Backscattered light at In-port
   
   #dB_tr=10*log10(D)
   #dB_back=10*log10(a)

   outfile.write(('%.10f %.10f\n') % (lamb, D))
   
   lamb += step

outfile.close()
#File_Graph(filename)

from pylab import plot, show, genfromtxt

data = genfromtxt("datos.dat", comments='#', unpack=True)

plot(data[0],data[1])

show()
