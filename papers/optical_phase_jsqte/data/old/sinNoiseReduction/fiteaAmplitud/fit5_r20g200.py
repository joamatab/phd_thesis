# -*- coding: utf-8 -*-
"""
10 V740D9_TEr20g200_Y 4001 amplitude line 10
normalize trace 11

10 V740D9_TEr20g200_Y 4001 fase line 12
normalize trace 13

#
"""

import sys
sys.path.append('/home/joaquin/Dropbox/python')
sys.path.append('/home/joaquin/Dropbox/reports/20121025_dispersionAnillos_/data')


#from pylab import savefig, unwrap,exp, pi, log10, plot, sqrt, log, show, interp, angle, figure, xlim, where, title,sin,pi
from pylab import *
from importa import importaa, importap
from scipy import optimize

def ring(x,phi=0,k=0.3,A=0.99,neff=4.36,R=20e-6):
#losses(dB/cm) = 20*log10(A)/(2*pi*20e-6*100)
    t = sqrt(1-k**2) if abs(k)<1.0 else 0
    A = abs(A) if abs(A)<1.0 else 0
    beta = 2* pi*neff/x
    L = 2* pi*R
   #plt.plot(x*1e9,20* log10( abs(Hcampo)))
   # plt.plot(x*1e9,(( angle(Hcampo)/pi)))
   # plt.ylabel('Fase de T/_p_i')
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
    
if __name__ == '__main__':
#overcoupled ring amplitude is trace number 10    
    
    amp='linearV740D9_TMrings_TErings.dat'
    
    xa,ya = importaa(amp)

    fitfunc = lambda p, x: field2dBnormalized(ring(x*1e-9,p[0],p[1],p[2],p[3])) # Target function
    errfunc = lambda p, x, y: fitfunc(p,x) - y # Distance to the target function
    
    index1560 = where(xa[10]>1560)[0][0]
#    index1560=-1
    indexTrace = 10
    indexTraceNoRing = 11
    
    xaOverCoupled=xa[indexTrace][0:index1560]
#    yaOverCoupled=(ya[indexTrace][0:index1560]-interp(xa[indexTrace][0:index1560],xa[indexTraceNoRing],ya[indexTraceNoRing]))
    yaOverCoupled=(ya[indexTrace][0:index1560]-interp(xa[indexTrace][0:index1560],xa[indexTraceNoRing],ya[indexTraceNoRing]))
    
    
    
    p0 = [8.93485182,0.48938045 , .9  , 4.3526515] # Initial guess for the parameters
    p1, success = optimize.leastsq(errfunc, p0[:], args=(xaOverCoupled, yaOverCoupled))
    print p0
    print p1

#    yfitdB = power2dBnormalized(yfit)
    subplot(211)
    grid()
    plot(xaOverCoupled,(yaOverCoupled),'-',xaOverCoupled,(fitfunc(p1,xaOverCoupled)),'--')
    ylabel('Transmission (dB)')
#    legend( ('data', 'fit'),loc='lower right' )
    yticks(arange(0,-16,-4),('0','-4','-8','-12'))
    xticks(arange(1530,1561,5),repeat('',shape(arange(1530,1561,5))[-1]))
#    title('Transmission')
   
#    xlim(1530,1560)

    phase='dispersionV740D9_TMringsTErings.dat'
    xp,yp = importap(phase)
    
#    +p[4]*(x-1530)+p[5]*(x-1530)**2+p[6]+p[7]*sin(2*pi*x/p[8])
    fitfunc2 = lambda p, x: unwrap(angle(ring(x*1e-9,p[0],p[1],p[2],p[3]))) # Target function
    errfunc2 = lambda p, x, y: fitfunc2(p,x) - y # Distance to the target function
    
    index1560 = where(xp[12]>1560)[0][0]
#    index1560=-1
    indexTrace = 12
    indexTraceNoRing = 13
    
    xpOverCoupled=xp[indexTrace][0:index1560]
    ypOverCoupled=-yp[indexTrace][0:index1560]+interp(xpOverCoupled,xp[indexTraceNoRing],yp[indexTraceNoRing])
#    ypOverCoupled=ypOverCoupled-ypOverCoupled[0]
    
#    p0 = [7*pi/4,0.5,30,4.36,-0.5,10e-3,2-3.45+1.25] # Initial guess for the parameters
    p0 = [7*pi/4,0.1,0.96983432,4.36,-0,0,0,0.2,1.9] # Initial guess for the parameters
    p2, success = optimize.leastsq(errfunc2, p0[:], args=(xpOverCoupled, ypOverCoupled))
    print p0
    print p2

    
    subplot(212)
    grid()
    plot(xpOverCoupled,ypOverCoupled/pi,xpOverCoupled,fitfunc2(p1,xpOverCoupled)/pi,'--')
    ylim([-13,1])
    yticks(-arange(0,13,2),('0','-2$\pi$','-4$\pi$','-6$\pi$','-8$\pi$','-10$\pi$','-12$\pi$'))
    ylabel('Phase (rad)')
    xlabel('Wavelength (nm)')
    legend( ('data', 'fit') )
#        plot(xpOverCoupled,ypOverCoupled,xpOverCoupled,unwrap(fitfunc2(p0,xpOverCoupled))) NO Es capaz de fitear la fase
#    title('Fit')
    savefig('r20g200TE.eps')
        
    show()
