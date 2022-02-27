clear all;
close all;
clc;

bits = [0 1 0 0 1 0 1 1 1 1 0]; 
bit_dur = 2;
fs = 100;

T = length(bits) * bit_dur;
t = 0:1/fs:T-(1/fs);

% bipolar AMI
last_bit = 1;
for i = 1:length(bits)
  if bits(i) == 0
    x((i-1)*fs*bit_dur+1:i*fs*bit_dur) = zeros(1, (fs*bit_dur));
  else
    x((i-1)*fs*bit_dur+1:i*fs*bit_dur) = ones(1, (fs*bit_dur)).*last_bit;
    last_bit = -last_bit;
  endif
endfor

plot(t, x, 'linewidth', 3);
ylim([-5,5]);
xlim([0,T]);

% demodulation
for i = 1:length(x)/(fs*bit_dur)
  if x((i-1)*fs*bit_dur+1:i*fs*bit_dur) == zeros(1, (bit_dur*fs))
    disp(0);
  else
    disp(1);
  endif
endfor
