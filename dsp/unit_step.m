N=21;
x=ones(1,N);
n=0:1:N-1;

hold on

subplot(3,2,1);
stem(n,x);
xlabel("n");
ylabel("x(n)");
title("Unit Step Sequence");


subplot(3,2,2);
stem(n, 0.8.^(n));
xlabel("n");
ylabel("x(n)");
title("Exponential Sequence");

subplot(3,2,3);
stem(n, n);
xlabel("n");
ylabel("x(n)");
title("Ramp Sequence");


subplot(3,2,4);
t = 0:0.01:pi
plot(t, sin(2*pi*t));
xlabel("n");
ylabel("x(n)");
title("Sinusoidal Sequence");

% y = x(t) = 5 sin 2*pi*1000*t + &
clear
a = 5;
ph = pi/2;
f = 2;
fs=10*f;
T=1;

t = 0:1/fs:T;
y = a * sin(2 * pi * f * t + ph);
subplot(3,2,5)
plot(t, y);
xlabel("t");
ylabel("x(t)");
title("Sinusoidal Sequence");


subplot(3,2,6)
stem(t, y);
xlabel("t");
ylabel("x(n)");
title("Discrete Sinusoidal Sequence");
