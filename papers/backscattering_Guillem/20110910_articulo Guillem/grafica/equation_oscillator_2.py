#
#Modelo de anillo basado en osciladores
#
#Aqui se encuentran las distintas ecuaciones asociadas al time-dependent model
#que esta descrito por ejemplo en el waves and fields in optoelectronics
#El desarrollo teorico de las ecuaciones pueden encontrarse en un paper de notch
#filters y coupling no se ke
#
#Guillem Ballesteros
#

def Through(x,Q_e1,Q_e2,Q_i,Q_u):
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

def Drop(x,Q_e1,Q_e2,Q_i,Q_u):
    """
    Los parametros del modelo son:
    tau_e1 -> tiempo de vida del foton asociado con el primer gap guia-anillo
    tau_e2 -> idem para el segundo gap
    tau_i  -> tiempo de vida del foton asociado a las perdidas intrinsecas
    u      -> constante de acoplamiento
    x      -> distancia al centro de la res (en frecuencia!!!) x-x0
    """
    from numpy import sqrt

    A = 2./Q_e1
    A_p = 2./Q_e2
    B = 1./Q_e1 + 1./Q_e2 + 1./Q_i
    u = 1./Q_u

    num = sqrt(A*A_p)*(2j*x + B)
    den = (2j*x + B)**2 + u**2

    return abs(num/den)**2

def AntiDrop(x,Q_e1,Q_e2,Q_i,Q_u):
    """
    Los parametros del modelo son:
    tau_e1 -> tiempo de vida del foton asociado con el primer gap guia-anillo
    tau_e2 -> idem para el segundo gap
    tau_i  -> tiempo de vida del foton asociado a las perdidas intrinsecas
    u      -> constante de acoplamiento
    x      -> distancia al centro de la res (en frecuencia!!!) x-x0
    """
    from numpy import sqrt


    A = 2./Q_e1
    A_p = 2./Q_e2
    B = 1./Q_e1 + 1./Q_e2 + 1./Q_i
    u = 1./Q_u

    num = sqrt(A*A_p)*u
    den = (2j*x + B)**2 + u**2

    return abs(num/den)**2


#Para ir probando las cosas
if __name__ == '__main__': 

    from matplotlib.pyplot import *
    from numpy import linspace
    x = linspace(-0.00017,0.00017,10000)
    
    Q_e1 = 66400.
    Q_e2 = 60500.
    Q_i  = 73200.
    Q_u  = 130000.

    T = Through(x,Q_e1,Q_e2,Q_i,Q_u) #azul
    D = Drop(x,Q_e1,Q_e2,Q_i,Q_u) #verde
    AD = AntiDrop(x,Q_e1,Q_e2,Q_i,Q_u) #rojo

    rcParams['figure.figsize'] = 4.2, 4.
    xticks([])
    grid(False)
    ax = gca()
    ax.set_yscale('log')
    yticks([1,0.1,0.01],['0','-10','-20'])
    ylim([0.005,1])
    ylabel('dB', fontsize='large')

    plot(x, T, x, D,x,AD)
    show()
