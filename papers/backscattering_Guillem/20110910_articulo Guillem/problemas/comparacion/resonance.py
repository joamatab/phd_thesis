#
#Version analitica del anillo con un punto de scattering
#
#

from cmath import e, pi
from numpy import linspace, cos, sqrt

##############
## Lambda_o ##
##############

lambda_o = 1.54898

########################
##  Factores Calidad  ##
########################

Q_e1 = 66378.949
Q_e2 = 1320515.825
Q_i  = 612938.6076
Q_u  = 588868.63093


###################################
##  Constantes importantes para  ##
##         la conversion         ##
###################################

neff = 4.3566; vg = 3e14/neff
radius = 20.; L = 2.*pi*radius
omega_o = 2*pi*3e14/lambda_o

########################################
## Constante space-domain calculadas  ##
##            con las Q               ##
########################################

K = omega_o*L/Q_e1/vg
R = (omega_o*L/2./Q_u/vg)**2

Q_loss = 1./( 1./Q_i + 1./Q_e2 )

alfa = omega_o/Q_loss/vg

############################
## ecuacion space-domain  ##
############################
a = e**(-1.*alfa*L/2.)

M = 1. - K
T = 1. - R

m = sqrt(M)
r = sqrt(R)
t = sqrt(T)


def T_space(lamb,m,t,a,neff,L):

   k = 2.*pi*neff/lamb
   m2 = m**2.
   t2 = t**2.
   a2 = a**2.
   
   A = m2*((a2-1.)**2.) + t2*a2*((m2+1.)**2.)
   B = (m2*a2 - 1.)**2. + 4.*m2*t2*a2
   
   c = cos(k*L)
   c2 = c**2.
   
   num = 4.*m2*a2*c2 - 2.*m*t*a*(m2+1.)*(a2+1.)*c + A
   den = 4.*m2*a2*c2 - 4.*m*t*a*(1. + m2*a2)*c + B
   
   return num/den 


###########################
## ecuacion time-domain  ##
###########################
def T_time(x,Q_e1,Q_e2,Q_i,Q_u):
    """
    Los parametros del modelo son:
    tau_e1 -> tiempo de vida del foton asociado con el primer gap guia-anillo
    tau_e2 -> idem para el segundo gap
    tau_i  -> tiempo de vida del foton asociado a las perdidas intrinsecas
    u      -> constante de acoplamiento
    x      -> distancia al centro de la res (en frecuencia!!!) x-x0
    """

    A = 2./Q_e1
    B = 1./Q_e1 + 1./Q_e2 + 1./Q_i
    u = 1./Q_u

    num = A*(2j*x + B)
    den = (2j*x + B)**2 + u**2

    return abs(1 - num/den)**2


#############################
##  Calcular space-domain  ##
#############################
x_space = linspace(1.40273,1.40492,35000)
y_space = T_space(x_space,m,t,a,neff,L)

x_space = 1.40376/x_space - 1.

##########################
## Calcular time-domain ##
##########################
x_time = linspace(-0.001,0.001,35000)
y_time = T_time(x_time,Q_e1,Q_e2,Q_i,Q_u)

###############
##  Grafica  ##
###############

from matplotlib.pyplot import *


xlim([-0.001,0.001])
plot(x_space,y_space)
plot(x_time,y_time)

#ax = gca()
#ax.set_yscale('log')

show()
