clear all;
close all;
clc;

bits = [1 0 0 0 0 0 0 0 0 1];
bit_dur = 2;
fs = 100;

T = length(bits) * bit_dur;
t = 0:1/fs:T-(1/fs);

counter = 0;
last_bit = 3;

for i = 1:length(bits)
  if bits(i) == 0
    counter = counter + 1
    if counter == 8
      x((i-1-7)*fs*bit_dur+1:(i-7)*fs*bit_dur) = 0;
      x((i-1-6)*fs*bit_dur+1:(i-6)*fs*bit_dur) = 0;
      x((i-1-5)*fs*bit_dur+1:(i-5)*fs*bit_dur) = 0;
      x((i-1-4)*fs*bit_dur+1:(i-4)*fs*bit_dur) = last_bit;
      x((i-1-3)*fs*bit_dur+1:(i-3)*fs*bit_dur) = -last_bit;
      last_bit = -last_bit;
      x((i-1-2)*fs*bit_dur+1:(i-2)*fs*bit_dur) = 0;
      x((i-1-1)*fs*bit_dur+1:(i-1)*fs*bit_dur) = last_bit;
      x((i-1)*fs*bit_dur+1:(i)*fs*bit_dur) = -last_bit;
      last_bit = -last_bit;
      counter = 0
    endif
  else
    counter = 0
    x((i-1)*fs*bit_dur+1:i*fs*bit_dur) = -last_bit;
    last_bit = -last_bit;
  endif
endfor

plot(t, x, 'linewidth', 3);
ylim([-5,5]);
title("B8ZS - Previous State is Negative");
grid on;


