from reflectivity import Reflectivity
import numpy as np
#Parametros fisicos
R = 0.000006
n_eff = 3.5
alfa_db = 5.


densidad_scat_points = 0.65 #puntos por micra
num_points = L*densidad_scat_points
num_points = int(num_points)

#Parametro simulacion
L_ini = 2.
L_end = 4000.
L_step = 150.

with open('Lreflectivity.dat', 'w') as outfile:
   outfile.write(('#R=%.8f; densidad=%.3f; alfa=%.2f\n') % (R,densidad_scat_points,alfa_db))

   #Lambda
   Lambda0 = np.arange(1.52,1.58,0.0000005)

   L = L_ini
   while L < L_end:

      #Array de puntos de scattering
      x = np.random.random_sample(size=num_points)*L
      x.sort()  #Esto me genera los puntos pero con el PlanB necesito la distancia
      #entre puntos y no su posicion
      d = np.zeros(len(x)+1)
      d[0]=x[0]
      d[-1]=L-x[-1]
      for i in range(len(d)-2):
         d[i+1]=x[i+1]-x[i]

      #Genero las matrices de scattering para cada lambda
      S = Reflectivity(R, Lambda0, n_eff, alfa_db, d)

      R2 = abs(S)**2.
      R_media = np.mean(R2)

      outfile.write('%.1f  %7.f\n' % (L,R_media))

      L += L_step

