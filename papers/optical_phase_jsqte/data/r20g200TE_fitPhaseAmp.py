# -*- coding: utf-8 -*-
"""
fitea la fase

noise reduction

10 V740D9_TEr20g200_Y 4001 amplitude line 10
normalize trace 11

10 V740D9_TEr20g200_Y 4001 fase line 12
normalize trace 13
#
"""

import sys
sys.path.append('/home/joaquin/Dropbox/python/importa')
sys.path.append('/home/joaquin/Dropbox/reports/20121025_dispersionAnillos/data')


from pylab import *
from importa import importaa, importap
from scipy import optimize


def ring(x,phi=0,k=0.3,A=0.99,ng=4.36,R=20e-6):
#losses(dB/cm) = 20*log10(A)/(2*pi*20e-6*100)
    t = sqrt(1-k**2) if abs(k)<1.0 else 0
    A = abs(A) if abs(A)<1.0 else 0
    beta = 2* pi*ng/x
    L = 2* pi*R
    return ( t-A* exp(1j*beta*L+1j*phi) )/( 1-t*A* exp(1j*beta*L+1j*phi) )
    
    
    
def normalizeSpectrum(y): 
    return 10*log10(abs(y))-max(10*log10(abs(y)))

def deNormalizeSpectrum(y): 
    return 10**(y/10)

def angleWithoutOffset(y): 
    return angle(y)-angle(y)[0]
    
def power2dBnormalized(x):
    return 10*log10(abs(x))-max(10*log10(abs(x)))

def field2dBnormalized(x):
    return 20*log10(abs(x))-max(20*log10(abs(x)))
    
def main():
#overcoupled ring amplitude is trace number 10    
    phase='dispersionV740D9_TMringsTErings.dat'
    xphase,yphase = importap(phase)
    indexTrace = 12
    indexTraceNoRing = 13
    
    index1560 = where(xphase[indexTrace]>1560)[0][0]
    xp=xphase[indexTrace][0:index1560]
    yp=yphase[indexTrace][0:index1560]
    
    dataShift=21
    yp=-yphase[indexTrace][0:index1560]+interp(xphase[indexTrace][dataShift:index1560+dataShift],xphase[indexTraceNoRing],yphase[indexTraceNoRing])
    
    amp='linearV740D9_TMrings_TErings.dat'
    xamp,yamp = importaa(amp)
    indexTraceNoRing = 11
    indexTrace= 10
    
    index1560 = where(xamp[10]>1560)[0][0]
    xa=xamp[indexTrace][0:index1560]
    ya=10**((yamp[indexTrace][0:index1560]-interp(xamp[indexTrace][0:index1560],xamp[indexTraceNoRing],yamp[indexTraceNoRing]))/20)
    ya=ya/max(ya)
    x=xa
    y=ya*exp(1j*yp)

 
    fitfunc = lambda p, x: ring(x*1e-9,p[0],p[1],p[2],p[3]) # Target function ring(x,phi=0,k=0.3,A=0.99,ng=4.36,R=20e-6)
    errfunc = lambda p, x, y: abs(real(fitfunc(p,x) - y)) +  abs(imag(fitfunc(p,x) - y)) # Distance to the target function
    p0 = [3,0.3 , .9  , 4.3526515] # Initial guess for the parameters
    
    p1, success = optimize.leastsq(errfunc, p0[:], args=(x, y))
    ax1 = subplot(211)
    plot(x,abs(y),'-',x,abs(fitfunc(p1,x)),'--')
    ylabel('Transmission')
    ax1.yaxis.set_label_coords(-0.1,0.5)


    title('$ 200nm-gap $ Overcoupled ring ($k=0.350$, $\mathrm{A=0.963}$, $n_g=4.36$)')
#    yticks(arange(0,1.1,0.2),('0','','','','','1'))
    yticks([0,1],('0','1'))
    xticks([1530,1560],['',''])
    

#    xticks(arange(1530,1561,5),repeat('',shape(arange(1530,1561,5))[-1]))


    print 'p0 = [phi,k,A,ng] = ',p0
    print 'p1 = [phi,k,A,ng] = ',p1
    a=p1[2]
    print 'losses = ',-log(a)/pi/(20e-6*100)*10/log(10)
    print 20*log10(p1[2])/(2*pi*20e-6*100)     
    
#    a=exp(-alfa*L/2)=exp(-alfa*2*pi*R/2)=exp(-alfa*pi*R)
#    log(a)=-alfa*pi*R
#    alfa = -log(a)/pi/R [m^-1]

    print -log(a)/pi/20e-4
    print 20*log10((p1[2])/(2*pi*20e-6*100))
    
    ax2 = subplot(212)
    ax2.yaxis.grid(True)
    plot(x,-unwrap(angle(y))/pi,x,-unwrap(angle(fitfunc(p1,x)))/pi,'--')
    ylabel('Phase (rad)')
    ola = ax2.yaxis.set_label_coords(-0.1,0.5)
    xlabel('Wavelength (nm)')
    legend( ('data', 'fit'),loc=8 )
    
    yticks([0,2,4,6,8,10,12],('$0$','$2\pi$','$4\pi$','$6\pi$','$8\pi$','$10\pi$','$12\pi$'))
#    xticks(arange(1530,1561,5),['1530','','','','','','1560'])
    xticks([1530,1560],['1530','1560'])
    savefig('r20g200TE_fitPhaseAmp.eps')
    show()
    return

    
if __name__ == '__main__':
        main()
