clear all
load v740tm_sz.m01
sz=v740tm_sz;



w=485;
h=220;
nmPerDivision=2000/1000;



aeff=w*h*1e-18*sum(sum(sz))/sum(sum(sz(round(500-w/4):round(500+w/4),round(500-h/4):round(500+h/4))))


figure(1)
imagesc(sz)
figure(2)
imagesc(sz(round(500-w/4):round(500+w/4),round(500-h/4):round(500+h/4)))

%3.2477e-13	
break
% n2= [332 , 47 , 361] .* [2.1420e-13, 3.2477e-13,  1.3410e-13] *1550e-9/2/pi *1e4/1e-9
% beta=2*[2.1420e-13, 3.2477e-13,  1.3410e-13].*[5.43, 5.44, 68.08]*1e11
% beta=2*[2.1420e-13, 3.2477e-13,  1.3410e-13].*[5.43, 5.44, 68.08]
