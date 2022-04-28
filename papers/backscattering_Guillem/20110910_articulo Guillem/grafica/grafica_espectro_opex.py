#
#
#Grafica con el espectro
#
#
from numpy import linspace,array,transpose,arange,log10
c = 2.99792E5 #metros*THz

from extract_resonance import extract_resonance   #Para obtener los datos exp.

name_in = 'medidas_nuevas.DAT'

import matplotlib.pyplot as p
from matplotlib.patches import Rectangle


from read_ring import read_data

data, nombres = read_data(name_in)


#Parametros genereles
p.rcParams['figure.figsize'] = 9, 9
p.subplots_adjust(bottom=0.07,top=0.96,wspace=0.13,right=0.95,left=0.1)

#import matplotlib.font_manager
#prop = matplotlib.font_manager.FontProperties(size=2)
#p.lagend(prop=prop) 



p.subplot(3,1,1)

p1,= p.plot(data[4][0],data[4][1],'r-',label=nombres[4][1])
p2,= p.plot(data[20][0],data[20][1],'b--',label=nombres[20][1])
p3,= p.plot(data[12][0],data[12][1],'g-.',label=nombres[12][1])

p.plot(data[5][0],data[5][1],'r-',label=nombres[5][1])
p.plot(data[21][0]+0.07,data[21][1],'b--',label=nombres[21][1])
p.plot(data[13][0]+0.07,data[13][1],'g-.',label=nombres[13][1])

p.plot(data[6][0],data[6][1],'r-',label=nombres[6][1])
p.plot(data[22][0]+0.07,data[22][1],'b--',label=nombres[22][1])
p.plot(data[14][0]+0.07,data[14][1],'g-.',label=nombres[14][1])

p.plot(data[7][0],data[7][1],'r-',label=nombres[7][1])
p.plot(data[23][0]+0.08,data[23][1],'b--',label=nombres[23][1])
p.plot(data[15][0]+0.08,data[15][1],'g-.',label=nombres[15][1])

p.plot(data[8][0],data[8][1],'r-',label=nombres[8][1])
p.plot(data[25][0]+0.05,data[25][1],'b--',label=nombres[24][1])
p.plot(data[16][0]+0.05,data[16][1],'g-.',label=nombres[16][1])

p.plot(data[9][0],data[9][1],'r-',label=nombres[9][1])
p.plot(data[26][0]+0.05,data[26][1],'b--',label=nombres[26][1])
p.plot(data[17][0]+0.05,data[17][1],'g-.',label=nombres[17][1])

p.xlim([1543,1568])
p.ylim([-45,-12])
p.xlabel('$\lambda$ (nm)')
p.ylabel('Transmission (dBm)', fontsize='small')
p.grid(True)
p.legend( (p1,p2,p3),  ('Through', 'Drop', 'Counter-Drop'), loc=4,prop=dict(size=12))

#Hacer una caja 
#p.fill([1548.69,1549.24,1549.24,1548.69], [-33,-33,-13,-13],alpha=0.,edgecolor='b')
p.text(1549.55,-16.7,'(a)')
p.text(1554.3,-16.7,'(b)')
p.text(1558.45,-16.7,'(c)')


#
#
#Los datos de los resultados del ajuste los ponemos justo en la grafica
#se hacen unos cuantos subplots mas vacios y dentro se mete el texto.
#
#ver http://matplotlib.sourceforge.net/users/gridspec.html

h1=p.subplot(3,3,4)

p.plot([], 'r')
p.xticks([])
p.yticks([])
p.grid(False)
#el texto
p.text(0.2,0.25,'$\\lambda_o$  = $1549.0$ $nm$\n$K_1$ = $3.35$ $\%$\n$K_2$ = $1.70$ $\%$\n$\\alpha$   =  $12.4$ $dB/cm$\n$\mathbf{R}$   = 0.036 %')


p.subplot(3,3,5)

p.plot([], 'r')
p.xticks([])
p.yticks([])
p.grid(False)
#p.text(0.2,0.25,'$\\lambda_o$  = 1553.4 nm\n$K_1$ = 3.33 %\n$K_2$ = 1.76 %\n$\\alpha$   =  11.2 dB/cm\n$R$   = 0.011 %')
p.text(0.2,0.25,'$\\lambda_o$  = $1553.4$ $nm$\n$K_1$ = $3.33$ $\%$\n$K_2$ = $1.76$ $\%$\n$\\alpha$   =  $11.2$ $dB/cm$\n$\mathbf{R}$   = 0.011 %')

p.subplot(3,3,6)

p.plot([], 'r')
p.xticks([])
p.yticks([])
p.grid(False)
#p.text(0.2,0.25,'$\\lambda_o$  = 1557.8 nm\n$K_1$ = 4.18 %\n$K_2$ = 1.96 %\n$\\alpha$   =  12.7 dB/cm\n$R$   = 0.18 %')
p.text(0.2,0.25,'$\\lambda_o$  = $1557.8$ $nm$\n$K_1$ = $4.18$ $\%$\n$K_2$ = $1.96$ $\%$\n$\\alpha$   =  $12.7$ $dB/cm$\n$\mathbf{R}$   = 0.18 %')

p.subplot(3,3,7)
###
#
#pico1
#
#
###############################################################################
###########                    Experimental Data                 ##############
###############################################################################
infile = 'medidas_nuevas.DAT'

Through_x_exp, Through_y_exp = extract_resonance(infile,5,0)
Drop_x_exp, Drop_y_exp = extract_resonance(infile,21,0)
AntiDrop_x_exp, AntiDrop_y_exp = extract_resonance(infile,13,0)

Drop_y_exp = Drop_y_exp/Through_y_exp.max()
AntiDrop_y_exp = AntiDrop_y_exp/Through_y_exp.max()
Through_y_exp = Through_y_exp/Through_y_exp.max()   #Normalizando el through a la unidad

omega0=c/1548.98

AntiDrop_x_exp = AntiDrop_x_exp -1548.905
Drop_x_exp = Drop_x_exp -1548.9
Through_x_exp = Through_x_exp   -1548.972 #Pasar a THz

##############################################################
#Un problemilla ahora es que vamos de mas frec a menos frec y por eso tenemos
#que reflejarlo todo ahora



################################################################################
#############              Horquilla de los datos                ###############
################################################################################

def Horquilla(Min, Max, x_exp, y_exp):
    """
    Te dan la frecuencia minima, la maxima los datos sobre los que hay que hacer
    la horquilla y los devuelve modificados
    """
    data = array([x_exp, y_exp])
    data = transpose(data)
    mod_data = [[x,y] for x,y in data if x > Min and x < Max]

    mod_data = transpose(mod_data)
    return mod_data[0], mod_data[1]

Through_x_exp, Through_y_exp = Horquilla(-0.2,0.2,Through_x_exp, Through_y_exp)
Drop_x_exp, Drop_y_exp = Horquilla(-0.2,0.2,Drop_x_exp, Drop_y_exp)
AntiDrop_x_exp, AntiDrop_y_exp = Horquilla(-0.2,0.2,AntiDrop_x_exp, AntiDrop_y_exp)

from equation_oscillator_2 import *

x = linspace(-0.0002,0.0002,5000)
Q_e1 = 66378.949
Q_e2 = 130515.825
Q_i  = 61938.6076
Q_u  = 58868.63093

#Renormalizando el espectro a lo que realmente se ha ajustado
new_base_line = 0.89
Drop_y_exp = Drop_y_exp/new_base_line
AntiDrop_y_exp = AntiDrop_y_exp/new_base_line
Through_y_exp = Through_y_exp/new_base_line

T = Through(x,Q_e1,Q_e2,Q_i,Q_u) #azul
D = Drop(x,Q_e1,Q_e2,Q_i,Q_u) #verde
AD = AntiDrop(x,Q_e1,Q_e2,Q_i,Q_u) #rojo

lambda0 = 1548.95
#Desnormalizando el eje de frecuencias
p.plot(-x*lambda0/(x+1)*10, 10*log10(T),'-.', lw=2.0)
p.plot(-x*lambda0/(x+1)*10, 10*log10(D),'-.', lw=2.0)
p.plot(-x*lambda0/(x+1)*10, 10*log10(AD),'-.', lw=2.0)

p.ylim([-25,0])
p.xlim([-2.01,2.01])
p.plot(Through_x_exp*10, 10*log10(Through_y_exp),'-')   #el *1e4 es un truquito para que no vaya jodiendo el pyplot con etiquetas de notacion cientifica
p.plot(Drop_x_exp*10, 10*log10(Drop_y_exp),'-')
p.plot(AntiDrop_x_exp*10, 10*log10(AntiDrop_y_exp),'-')
p.ylabel('Transmission (dB)',fontsize='small')
#p.xlabel('$\omega\'-1 $')
p.ticklabel_format(style='sci',scilimits=(2,2),axis='x')

p.text(0.37,-3.94,'T')
p.text(0.88,-13.03,'D')
p.text(0.54,-21.00,'C')

#texto
p.text(1.565,-2.37,'(a)')

p.subplot(3,3,8)

###
#
#pico1
#
#
###############################################################################
###########                    Experimental Data                 ##############
###############################################################################
infile = 'medidas_nuevas.DAT'

Through_x_exp, Through_y_exp = extract_resonance(infile,6,0)
Drop_x_exp, Drop_y_exp = extract_resonance(infile,22,0)
AntiDrop_x_exp, AntiDrop_y_exp = extract_resonance(infile,14,0)

Drop_y_exp = Drop_y_exp/Through_y_exp.max()
AntiDrop_y_exp = AntiDrop_y_exp/Through_y_exp.max()
Through_y_exp = Through_y_exp/Through_y_exp.max()   #Normalizando el through a la unidad

omega0=c/1553.36

AntiDrop_x_exp = AntiDrop_x_exp - 1553.286
Drop_x_exp = Drop_x_exp -1553.284
Through_x_exp = Through_x_exp -1553.3588     #Pasar a THz

##############################################################
#Un problemilla ahora es 


################################################################################
#############              Horquilla de los datos                ###############
################################################################################


Through_x_exp, Through_y_exp = Horquilla(-0.2,0.2,Through_x_exp, Through_y_exp)
Drop_x_exp, Drop_y_exp = Horquilla(-0.2,0.2,Drop_x_exp, Drop_y_exp)
AntiDrop_x_exp, AntiDrop_y_exp = Horquilla(-0.2,0.2,AntiDrop_x_exp, AntiDrop_y_exp)

from equation_oscillator_2 import *

x = linspace(-0.0002,0.0002,5000)
Q_e1 = 66421.832
Q_e2 = 126071.59
Q_i  = 68502.438
Q_u  = 105389.748


#Renormalizando el espectro a lo que realmente se ha ajustado
new_base_line = 0.94
Drop_y_exp = Drop_y_exp/new_base_line
AntiDrop_y_exp = AntiDrop_y_exp/new_base_line
Through_y_exp = Through_y_exp/new_base_line

T = Through(x,Q_e1,Q_e2,Q_i,Q_u) #azul
D = Drop(x,Q_e1,Q_e2,Q_i,Q_u) #verde
AD = AntiDrop(x,Q_e1,Q_e2,Q_i,Q_u) #rojo

lambda0 = 1553.36
#Desnormalizando el eje de frecuencias
p.plot(-x*lambda0/(x+1)*10, 10*log10(T),'-.', lw=2.0)
p.plot(-x*lambda0/(x+1)*10, 10*log10(D),'-.', lw=2.0)
p.plot(-x*lambda0/(x+1)*10, 10*log10(AD),'-.', lw=2.0)

p.ylim([-25,0])
p.xlim([-2.01,2.01])
p.plot(Through_x_exp*10, 10*log10(Through_y_exp),'-')
p.plot(Drop_x_exp*10, 10*log10(Drop_y_exp),'-')
p.plot(AntiDrop_x_exp*10, 10*log10(AntiDrop_y_exp),'-')
p.yticks([0,-5,-10,-15,-20,-25],[' ',' ',' ',' ',' '])            # don't want to see any ticks on this axis
p.xlabel('$\Delta\lambda (\\times10^{-1})$ (nm)')#,fontsize='large')
p.ticklabel_format(style='sci',scilimits=(2,2),axis='x')
p.text(1.565,-2.37,'(b)')

p.text(0.385,-3.94,'T')
p.text(0.83,-13.03,'D')
p.text(0.36,-21.00,'C')

p.subplot(3,3,9)
###
#
#pico1
#
#
###############################################################################
###########                    Experimental Data                 ##############
###############################################################################
infile = 'medidas_nuevas.DAT'

Through_x_exp, Through_y_exp = extract_resonance(infile,7,0)
Drop_x_exp, Drop_y_exp = extract_resonance(infile,23,0)
AntiDrop_x_exp, AntiDrop_y_exp = extract_resonance(infile,15,0)

Drop_y_exp = Drop_y_exp/Through_y_exp.max()
AntiDrop_y_exp = AntiDrop_y_exp/Through_y_exp.max()
Through_y_exp = Through_y_exp/Through_y_exp.max()   #Normalizando el through a la unidad

omega0=c/1557.79

AntiDrop_x_exp = AntiDrop_x_exp -1557.704
Drop_x_exp = Drop_x_exp -1557.708
Through_x_exp = Through_x_exp -1557.7888      #Pasar a THz

##############################################################



################################################################################
#############              Horquilla de los datos                ###############
################################################################################



Through_x_exp, Through_y_exp = Horquilla(-0.2,0.2,Through_x_exp, Through_y_exp)
Drop_x_exp, Drop_y_exp = Horquilla(-0.2,0.2,Drop_x_exp, Drop_y_exp)
AntiDrop_x_exp, AntiDrop_y_exp = Horquilla(-0.2,0.2,AntiDrop_x_exp, AntiDrop_y_exp)

from equation_oscillator_2 import *

x = linspace(-0.0002,0.0002,5000)
Q_e1 = 52833.569
Q_e2 = 112499.15
Q_i  = 59880.011
Q_u  = 25725.31

#Renormalizando el espectro a lo que realmente se ha ajustado
new_base_line = 0.92
Drop_y_exp = Drop_y_exp/new_base_line
AntiDrop_y_exp = AntiDrop_y_exp/new_base_line
Through_y_exp = Through_y_exp/new_base_line

T = Through(x,Q_e1,Q_e2,Q_i,Q_u) #azul
D = Drop(x,Q_e1,Q_e2,Q_i,Q_u) #verde
AD = AntiDrop(x,Q_e1,Q_e2,Q_i,Q_u) #rojo

lambda0 = 1557.79
#Desnormalizando el eje de frecuencias
p.plot(-x*lambda0/(x+1)*10, 10*log10(T),'-.', lw=2.0)
p.plot(-x*lambda0/(x+1)*10, 10*log10(D),'-.', lw=2.0)
p.plot(-x*lambda0/(x+1)*10, 10*log10(AD),'-.', lw=2.0)


p.ylim([-25,0])
p.xlim([-2.01,2.01])
p.plot(Through_x_exp*10, 10*log10(Through_y_exp),'-')
p.plot(Drop_x_exp*10, 10*log10(Drop_y_exp),'-')
p.plot(AntiDrop_x_exp*10, 10*log10(AntiDrop_y_exp),'-')
p.yticks([0,-5,-10,-15,-20,-25],[' ',' ',' ',' ',' '])              # don't want to see any ticks on this axis
#p.xticks([-2,-1,0,1,2],[' ',' ',' ',' '])
p.text(1.565,-2.37,'(c)')

p.text(0.68,-3.94,'T')
p.text(1.05,-13.03,'D')
p.text(1.00,-21.00,'C')

#p.xlabel('$\omega\'-1 $')
p.ticklabel_format(style='sci',scilimits=(2,2),axis='x')
p.show()
