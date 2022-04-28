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


#from pylab import savefig, unwrap,exp, pi, log10, plot, sqrt, log, show, interp, angle, figure, xlim, where, title,sin,pi
from pylab import *
from importa import importaa, importap
from scipy import optimize


def ring(x,phi=0,k=0.3,A=0.99,ng=4.36,R=20e-6):
#losses(dB/cm) = 20*log10(A)/(2*pi*20e-6*100)
    t = sqrt(1-k**2) if abs(k)<1.0 else 0
    A = abs(A) if abs(A)<1.0 else 0
    beta = 2* pi*ng/x
    L = 2* pi*R
    return (  t-A* exp(1j*beta*L+1j*phi)  )/(  1-t*A* exp(1j*beta*L+1j*phi)  )

    
    
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
    indexTrace = 14
    indexTraceNoRing = 13
    
    index1560 = where(xphase[indexTrace]>1560)[0][0]
    xp=xphase[indexTrace][0:index1560]
    yp=yphase[indexTrace][0:index1560]
    
    dataShift=21
    yp=-yphase[indexTrace][0:index1560]+interp(xphase[indexTrace][dataShift:index1560+dataShift],xphase[indexTraceNoRing],yphase[indexTraceNoRing])
    
    amp='linearV740D9_TMrings_TErings.dat'
    xamp,yamp = importaa(amp)
    indexTraceNoRing = 11
    indexTrace= 12
    
    index1560 = where(xamp[10]>1560)[0][0]
    xa=xamp[indexTrace][0:index1560]
    ya=10**((yamp[indexTrace][0:index1560]-interp(xamp[indexTrace][0:index1560],xamp[indexTraceNoRing],yamp[indexTraceNoRing]))/20)
    ya=ya/max(ya)
    
    x=xa
    y=ya*exp(1j*yp)
    
    fitfunc = lambda p, x: ring(x*1e-9,p[0],p[1],p[2],p[3]) # Target function
    errfunc = lambda p, x, y: abs(real(fitfunc(p,x) - y))+abs(imag(fitfunc(p,x) - y)) # Distance to the target function
    
    p0 = [8.8,0.3 , .9  , 4.3526515] # Initial guess for the parameters
    
    p1, success = optimize.leastsq(errfunc, p0[:], args=(x, y))
    ax1 = subplot(211)
    plot(x,abs(y),'-',x,abs(fitfunc(p1,x)),'--')
    ylabel('Transmission')
    ax1.yaxis.set_label_coords(-0.1,0.5)
    legend( ('data', 'fit'),loc=8)
    title('$ 275nm-gap $ Undercoupled ring ($k=0.217$, $\mathrm{A=0.934}$, $n_g=4.35$)')
    yticks([0,1],('0','1'))
    xticks([1530,1560],['',''])

    print 'p0='
    print p0

    a = p1[2]
    print 'p1='
    print p1    
    alpha =  -log(a**2)/(2*pi*20e-6*100) # cm^-1
    alphadBcm =  -log(a**2)/(2*pi*20e-6*100) # cm^-1
    
    
    ax2 = subplot(212)
    plot(x,angle(y)/pi,x,angle(fitfunc(p1,x))/pi,'--')
    ylabel('Phase (rad)')
    ax2.yaxis.set_label_coords(-0.1,0.5)
    xlabel('Wavelength (nm)')
    yticks([-0.5,.5],('$-\pi/2$','$\pi/2$'))
    
    xticks([1530,1560],['1530','1560'])
    savefig('r20g275TE_fitPhaseAmp.eps')
    show()
    return
    
#     yticks(arange(0,1.1,0.2),('0','','','','','1'))   
#    yticks([-0.25,-.125,0,0.125,.25],('$-\pi/4$','$-\pi/8$','$0$','$\pi/8$','$\pi/4$'))
    
if __name__ == '__main__':
        main()
