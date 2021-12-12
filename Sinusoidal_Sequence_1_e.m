% Sinusoidal Sequence:
f = 1000
T=1;
fs = 10 * f;
t = 0:1/fs:T;

y = sin(2*pi*t*f);
%stem(t, y);
plot(t, y);
xlabel('e');
ylabel('Amplitude');
title('Sinusoidal Sequence');