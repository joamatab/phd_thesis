% aeff P13
load modeP13_ey.m01

(sum(sum(modeP13_ey.^2)))^2/sum(sum((modeP13_ey(501-118:501+118,501-69:501+70).^4)))*1.998e-3^2

%0.8836

break

(sum(sum(modeP13_ey.^2)))^2/sum(sum((modeP13_ey.^4)))*1.998e-3^2

%0.2902

