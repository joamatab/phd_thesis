load tm0p01_ey.m00
imagesc(tm0p01_ey)

modo=tm0p01_ey;
imagesc(modo)
4*0.01*0.01*( sum(sum(modo.^2)) )^2/( sum(sum(modo(1:23,1:10).^4)) )
4*0.01*0.01*( sum(sum(modo.^2)) )^2/( sum(sum(modo(1:24,1:10).^4)) )

break
/rn,a,b/nx0/ls1
/r,qa,qb
151 0 1.5 0 OUTPUT_REAL_3D 1.631322861 6.093635534e-07
151 0 1.5
