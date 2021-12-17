clear all;
close all;
clc;

bits = [0 1 0 1 1 0 1 1 1 0 1 1 0];
bit_dur = 100;

T = length(bits)*bit_dur;
fs = 2;

t = 0:1/fs:T-(1/fs);

% assume upper voltage 3, mid  neutral and lower voltage -3
voltage = 3;
count = 0;
for i = 1:length(bits)
  if bits(i) == 0 && i == 1
    x((i-1)*fs*bit_dur+1:i*fs*bit_dur) = zeros(1, fs*bit_dur);
  elseif bits(i) == 1
    count = count + 1; 
    if mod(count,4) == 1 && count == 1
      x((i-1)*fs*bit_dur+1:i*fs*bit_dur) = ones(1, fs*bit_dur).*voltage;
    elseif mod(count,4) == 1
      x((i-1)*fs*bit_dur+1:i*fs*bit_dur) = ones(1, fs*bit_dur).*voltage;
    elseif mod(count,4) == 2
      x((i-1)*fs*bit_dur+1:i*fs*bit_dur) = zeros(1, fs*bit_dur).*voltage; 
    elseif mod(count,4) == 3
      x((i-1)*fs*bit_dur+1:i*fs*bit_dur) = ones(1, fs*bit_dur).*voltage;
    elseif mod(count,4) == 0
      x((i-1)*fs*bit_dur+1:i*fs*bit_dur) = ones(1, fs*bit_dur).*voltage;
    endif
  else
    x((i-1)*fs*bit_dur+1:i*fs*bit_dur) = ones(1, fs*bit_dur).*voltage;
  endif
endfor

plot(t, x);
ylim([-5,5]);
xlim([0,T]);