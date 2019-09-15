"""
Calcula la salida de un anillo con un solo pto
de scattering. De forma analitica modificando
un par de comentarios y la salida del archivo podemos hacer
que recorra lambda o k segun necesitemos
"""

from cmath import sqrt, pi, e 
from numpy import cos, linspace
from pylab import plot, show

#give an output filename is you wish to do so
#import sys
#try:
#   filename = sys.argv[1]
#except IndexError:
#   filename = 'datos.dat'


####PHYSICAL CONSTANTS#####
radius = 15.
L = 2. * pi *radius
neff = 3.5

R = 0.001
K = 0.0529
#T = 1. - R
#M = 1. - K
#
#alfa = 2.  #db/cm
#alfa /= 4.34294482
#alfa *= (10**-4.)
#a = e**(-1.*alfa*L)
#
#m = sqrt(M)    #The other part to k
#r = sqrt(R)
#t = sqrt(T)/a
#T = t**2.
#gamma = T + R

####SIMULATION PARAMETERS####
Lambda = linspace(1.45,1.55,1000)

#Open output file
#outfile = open(filename, 'w')


#k0 = k_ini
#while k0 < k_end:
#lamb = lamb_ini
#while lamb < lamb_end:   
#   
#   #k = k0 *neff
#   k = 2.*pi*neff/lamb
#
#
#   A = t*(M + 1.)
#   c = cos(k*L)
#   c2 = cos(k*L)**2.
#   
#   D1 = 4.*M*c2 - 4.*m*A*c + (A**2.) 
#   D2 = 4.*M*c2 - 4.*m*A*c + (M - 1.)**2. + 4.*M*T
#   
#   outfile.write(('%.10f %.10f \n') % (lamb, D1/D2))
#
#   #k0 += step
#   lamb += step
#
#outfile.close()

def Through(lamb, radius, neff, K, R):
    T = 1. - R
    M = 1. - K

    alfa = 2.  #db/cm
    alfa /= 4.34294482
    alfa *= (10**-4.)
    a = e**(-1.*alfa*L)

    m = sqrt(M)    #The other part to k
    r = sqrt(R)
    t = sqrt(T)/a
    T = t**2.

    k = 2.*pi*neff/lamb


    A = t*(M + 1.)
    c = cos(k*L)
    c2 = cos(k*L)**2.
   
    D1 = 4.*M*c2 - 4.*m*A*c + (A**2.) 
    D2 = 4.*M*c2 - 4.*m*A*c + (M - 1.)**2. + 4.*M*T

    return D1/D2

T = Through(Lambda, radius, neff, K, R)

plot(Lambda, T)
show()



