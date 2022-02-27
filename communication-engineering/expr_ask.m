close all;
clear all;
clc;

bits = [0 1 1 1 0 0 0 1 0 1];
bit_dur = 1;
fs = 100;

T = length(bits) * bit_dur;
t = 0:1/fs:T-(1/fs);

for i = 1:length(bits)
  if bits(i) == 0
    x((i-1)*fs*bit_dur+1:i*fs*bit_dur) = zeros(1, fs*bit_dur);
  else
    x((i-1)*fs*bit_dur+1:i*fs*bit_dur) = ones(1, fs*bit_dur);
  endif
endfor

subplot(3,1,1);
plot(t, x, 'linewidth', 3);
ylim([-3, 3]);
title("Input Signal");

a = 5;
f = 3;

sig = a * sin ( 2* pi * f * t);
subplot(3,1,2);
plot(t, sig);
title("Carrier signal"); 


% Modulation
m = x.*sig;
subplot(3,1,3);
plot(t, m);
title("ASK"); 

% Demodulation
