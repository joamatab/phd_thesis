clear all
load p13_sz.m01



w=475;
h=253;
nmPerDivision=2000/1000;



aeff=w*h*1e-18*sum(sum(p13_sz))/sum(sum(p13_sz(round(500-w/4):round(500+w/4),round(500-h/4):round(500+h/4))))



%2.1420e-13
break
figure(1)
imagesc(p13_sz)
figure(2)
imagesc(p13_sz(round(500-w/4):round(500+w/4),round(500-h/4):round(500+h/4)))


