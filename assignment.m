% given = 5sin(2*pi*1000*t+d)
subplot(2, 1, 1);
f = 10;
t = 0:1/(f*100):1;
d = 0;
y = 5 * sin(2*pi*f*t + d);
plot(t, y);
xlabel('---> t');
ylabel('Amplitude');
title('Analog form');

% discrete form
subplot(2, 1, 2);
%fs = input('Enter the sampling frequency: ');
fs = 10 * f;
n = 0:1:100;
y2 = 5 * sin(2*pi*(f/fs)*n + d);
stem(n, y2);
xlabel('---> n');
ylabel('Amplitude');
title('Discrete form')