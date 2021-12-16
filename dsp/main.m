% x(t) = 2 sin 2pi 1000 t

clc;
clear all;

% sin wave
a = 2;
f = 1000;

t = 0:0.00001:.02;
y = a * sin ( 2 * pi * t * f);

hold on
subplot(4,2,1);
plot(t, y);

% discrete signal
N = 500;
n = 0:N-1;
fs = 20 * f;

y = a * sin ( 2 * pi * (f/fs) * n)
subplot(4,2,2);
plot(n, y);


% hamming window
N_temp = 100;
n_temp = 0:N_temp-1;

hw = 0.54 - 0.46 * cos ((2 * pi * n_temp) / (N_temp-1));
pad_hw = [zeros(1,200), hw, zeros(1,200)]
subplot(4,2,3);
plot(n,pad_hw)



% multiply with hamming
yw = y .* pad_hw;
subplot(4,2,4)
plot(yw)

% recangular window
rw=[zeros(1,200) ones(1,100), zeros(1,200)]
subplot(4,2,5)
plot(n,rw);

% multiply with rectangular window
yw = y .* rw;

subplot(4,2,6)
plot(yw)


% triangular window
N_temp = 100;
n_temp = 0:N_temp-1;
tw  = 1 - (abs(2*n_temp - N_temp + 1)/(N_temp-1))  
pad_tw = [zeros(1,200), tw, zeros(1,200)]
subplot(4,2,7);
plot(n,pad_tw)


% multiply with triangular window
yw = y .* pad_tw;

subplot(4,2,8)
plot(n,yw)
