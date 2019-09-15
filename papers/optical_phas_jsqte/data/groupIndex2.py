# -*- coding: utf-8 -*-
"""

plota plots the amplitud of dataset selected graphs or all them if -1 into a graph
plotp plots the phase

xdata(nm),ydata(dB) = importaAmp(aa)
xdata(nm),ydata(rad) = importaPhase(aa)

"""

import sys
sys.path.append('/home/joaquin/Dropbox/python/importa')
from pylab import *
from importa import importap, importaa

def main():
    #corrugated 6 (27\mum)','corrugated 1 (450\mum)
    x6,y6 = importap('/home/joaquin/Dropbox/reports/20110724_DispersionSara/dataJoaquin/corrugada6_setbottom_scan_all.dat',[0])
    x1,y1 = importap('/home/joaquin/Dropbox/reports/20110724_DispersionSara/dataJoaquin/corrugada1_setbottom_C11_Pin=-1.dat',[0])
    c=3e8
    x1t = x1[0][31:300] # from 1569 to 1596~nm
    y1t = y1[0][31:300]
    x6t = x6[0]
    y6t = y6[0]
    w1 = 2*pi*c/(x1t*1e-9)-2*pi*c/1574e-9
    yw1 = y1t
    w6 = 2*pi*c/(x6t*1e-9)-2*pi*c/1564e-9
    yw6 = y6t   
    xmin = 1e-6*array([ 1.563778713098983,   1.564429468006409,   1.565494339673106,   1.566559211339802,   1.568038199765770,   1.569517188191737,   1.571232814765860,   1.573007600877021,   1.575196503747453,   1.577267087543807,   1.579810947636471,   1.581999850506903,   1.584129593840296,   1.586495975321844,   1.588684878192276,   1.591051259673824,   1.592589407636830,   1.595014948655417,   1.596553096618423,   1.598327882729584,   1.599511073470358,   1.600990061896326,   1.602232412174138,   1.603297283840835,   1.604184676896416])    
    x=linspace(min(xmin),max(xmin),len(yw6))
    w = 2*pi*3e8/x-2*pi*3e8/1574e-9
        
    orderPol = 5
    p1 = polyfit(w1,yw1,orderPol)
    p6 = polyfit(w6,yw6,orderPol) 
    figure(2)
    plot(x1t,yw1,x6t,yw6,x1t,polyval(p1,w1),x6t,polyval(p6,w6),x1t,polyval(p1-p6,w1))

    figure(3)
    subplot(212)
    plot(x*1e9,7.8-c/423e-6*polyval(polyder(p1-p6),w),'b-')
  
    ax=subplot(211)
    ax.set_title('(a)',ha='left',)
              
    aa='/home/joaquin/Dropbox/reports/20121025_dispersionAnillos/data/linear_santec0dBm_V740_C11_MiddleSet_18deg_corrugadas_Antoine.dat'
    xmzi,ymzi = importaa(aa,[0,1],0)
    

    xmin = 1e-6*array([ 1.563778713098983,   1.564429468006409,   1.565494339673106,   1.566559211339802,   1.568038199765770,   1.569517188191737,   1.571232814765860,   1.573007600877021,   1.575196503747453,   1.577267087543807,   1.579810947636471,   1.581999850506903,   1.584129593840296,   1.586495975321844,   1.588684878192276,   1.591051259673824,   1.592589407636830,   1.595014948655417,   1.596553096618423,   1.598327882729584,   1.599511073470358,   1.600990061896326,   1.602232412174138,   1.603297283840835,   1.604184676896416])
    ymin = array([-30.112883270882282, -30.319110314265075, -31.040904966104854, -32.037669009121686, -33.137546573829916, -34.031197095155349, -35.612271094423434, -37.090231572000121, -37.708912702148496, -41.420999483038770, -42.658361743335533, -42.830217612821194, -48.054636045185291, -44.273806916500746, -47.848409001802494, -46.164221480843018, -47.917151349596757, -49.223255957687783, -48.707688349230800, -50.976185826441522, -51.801093999972693, -51.251155217618582, -51.319897565412845, -53.554023868726439, -51.732351652178437])
    xmax = 1e-6*array([1.564133670321216,   1.564961903839758, 1.566026775506454,   1.567150806710189,1.568748114210234,1.570227102636202,   1.571942729210324,   1.574249951154833,1.576083896803033,   1.578331959210504,1.580757500229090,   1.583301360321754,   1.585312784581070,   1.587383368377425,   1.589868068933050,   1.591997812266443,   1.593890917451682,   1.595665703562843,   1.597440489674004,   1.598682839951816,   1.600161828377784,   1.601640816803751,   1.602764848007487,   1.603474762451951,   1.604598793655686])
    ymax=array([-29.700429184116697, -29.597315662425299, -29.562944488528167, -30.112883270882282, -29.459830966836773, -29.666058010219565, -30.284739140367943, -31.144018487796249, -31.762699617944627, -32.793834834858593, -33.378144791109840, -34.306166486332408, -34.924847616480790, -36.987118050308723, -37.468314484868571, -39.221244353622311, -40.939803048478922, -41.317885961347379, -43.620754612455229, -43.792610481940898, -47.092243176065587, -47.332841393345511, -47.092243176065587, -47.882780175699622, -50.701216435264470])

    xlim(1563,1605)
    ylim(-55,-29)
    xticks([1570,1600],('',''))
    yticks([-30,-55],('-30','-55',))
    ylabel('Transmission (dB)')
    ax.yaxis.set_label_coords(-0.1,0.5)
    plot(xmzi[0],ymzi[0],'b-',xmin*1e9,ymin,'go',xmax*1e9,ymax,'go')
    legend()
    

    ax2 = subplot(212)
    title('(b)')
    ng2 = (xmin*xmax)/2/450e-6/abs(xmin-xmax) + 4.36    
    
    plot(xmin*1e9,ng2,'go')
    xlabel('Wavelength (nm)')
    ylabel('Group index')
    xticks([1570,1600],('1570','1600'))
    yticks([7,9,11,13],('7','9','11','13'))
    xlim(1563,1605)
    ylim([6,14])
    legend(('Heterodyne','fringes'), loc=9)
    savefig('gropIndexComparison_2.png')
    savefig('gropIndexComparison_2.eps')
    show()
    return
    
    
#    legend(('Heterodyne','fringes'), ncol=2, mode="expand", loc=2)
    
    
#    legend(["Heterodyne"], loc=1, ["fringes"], loc=4)
#    l2 = legend([p2], ["fringes"], loc=4) # this removes l1 from the axes.
#    gca().add_artist(l1) # add l1 as a separate artist to the axes
    
#    ng2 = 1580e-9**2/diff(xmax*1e-9)/450e-6 + 4.36
#    plot(xmax[0:-1],ng2,'+')



 # this is another inset axes over the main axes
#    a = axes([0.25, 0.5, .5, .3], axisbg='y')
    

#    setp(a, xlim=(1563,1605),ylim=(-55,-29), xticks=[],yticks=[])


#    w1 = 2*pi/(x1t*1e-9) -2*pi/1585e-9
#    yw1 = y1t
#    
#    w6 = 2*pi/(x6[0]*1e-9) -2*pi/1585e-9
#    yw6 = y6[0]
#    
#    orderPol = 6
#    
#    
##    approximate_taylor_polynomial(y,0,2,1)
#    
#    p1 = polyfit(w1,yw1,orderPol)
#    p6 = polyfit(w6,yw6,orderPol)    
#    
#    plot(w1,yw1,w6,yw6)
    
   



if __name__ == '__main__':
    main()
