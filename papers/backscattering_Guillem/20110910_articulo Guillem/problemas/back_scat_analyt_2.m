clear
syms delta_w through0 drop0 coundrop0 coundrop coundrop_h through drop Q Qe1 Qe2 Qeff QR A B positive

A = delta_w/sqrt((coundrop0/drop0)-1+sqrt(2)*sqrt((coundrop0/drop0)^2+1));
B = A*sqrt(coundrop0/drop0);

Q = 1/A;
Qe1 = 2*A/((A^2+B^2)*(1+sqrt(through0)));
Qe2 = 2*A*(1+sqrt(through0))/(drop0*(A^2+B^2));
QR = 1/B;

Qeff = sqrt(Qe1*Qe2);

through = (1-2/(Qe1*Q*(1/Q^2+1/QR^2)))^2
drop = (2/(Q*Qeff*(1/Q^2+1/QR^2)))^2
coundrop = (2/(QR*Qeff*(1/Q^2+1/QR^2)))^2
coundrop_h = simplify(abs(2/(QR*Qeff*((2*1i*delta_w/2+1/Q)^2+1/QR^2)))^2)

