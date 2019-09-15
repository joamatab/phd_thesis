#
#Programa para simular el campo reflejado suponiendo multi scattering
#en realidad no es mas que el modulo del S11 de la matriz de scattering
#

import numpy as np
from numpy import sqrt, array, pi, exp ,zeros

def Reflectivity(R, lambda0, n_eff, alfa_dB, x_i):
   "Usando transfer matrix"
   #Los arrays de S11 xa cada longitud de onda
   S11 = zeros(len(lambda0),complex)
   
   r = sqrt(R)
   t = sqrt(1.-R)
   
   #variables fisicas
   k = 2*pi*n_eff/lambda0
   alfa = alfa_dB * (10**-4.)/4.34294482
   
   aux_k = (1j*k - alfa/2.)
   
   for m in range(len(aux_k)):
      aux1 = array([[1,0],[0,1]],complex) #la variable intermedia que guarda el producto de matrices
      
      for z in range(len(x_i)-1):
         aux2_1=exp( aux_k[m]*x_i[z])
         aux2_2=exp(-aux_k[m]*x_i[z])
         
         aux2 = array([[aux2_1,-r*aux2_2],[-r*aux2_1,aux2_2]],complex)
         aux1 = dot(aux2,aux1)
         
      CC_1=aux_k[m]*x_i[-1]
      CerrarCamino = array([[exp(CC_1),0],[0,exp(-CC_1)]],complex)
      Trx = dot(CerrarCamino,aux1)/( t**float(len(x_i)) )
      
      
      S11[m] = Trx[0][1]/Trx[1][1]

      
   return S11

