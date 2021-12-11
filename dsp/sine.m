% y = x(t) = 5 sin 2*pi*1000*t + &
clear
a = 5;
ph = 0;
f = 1000;
fs=20*f;
T=0.004;



hold on
t = 0:1/fs:T;
y = a * sin(2 * pi * f * t + ph);
subplot(2,1,1)
plot(t, y);
subplot(2,1,2)
stem(t, y);