load TEmode0p01_ex.m00
imagesc(TEmode0p01_ex)


modo=TEmode0p01_ex;
imagesc(modo)
4*0.01*0.01*( sum(sum(modo.^2)) )^2/( sum(sum(modo(1:21,1:10).^4)) )

break
/rn,a,b/nx0/ls1
/r,qa,qb
151 0 1.5 0 OUTPUT_AMPLITUDE_3D 2.222486734 4.546826204e-08
151 0 1.5
