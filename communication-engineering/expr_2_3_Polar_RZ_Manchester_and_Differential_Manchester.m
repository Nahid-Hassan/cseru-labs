clear all;
close all;
clc;

bits = [0 1 0 0 1 1];
bit_dur = length(bits);

fs = 100;
T = length(bits) * bit_dur;

t = 0:1/fs:T-(1/fs);

% Polar RZ Modulation
one = [ones(1, (fs/2)*bit_dur).*3, zeros(1,(fs/2)*bit_dur)];
zero = [ones(1, (fs/2)*bit_dur).*-3, zeros(1,(fs/2)*bit_dur)];

for i = 1:length(bits)
  if bits(i) == 1
    polar_rz((i-1)*fs*bit_dur+1:i*fs*bit_dur) = one;
  else
    polar_rz((i-1)*fs*bit_dur+1:i*fs*bit_dur) = zero;
  endif
endfor



subplot(3,1,1);
plot(t, polar_rz, 'linewidth', 3);
ylim([-5,5]);
xlim([0,T]);
grid on;
title("Polar RZ");

% demodulation Polar RZ
disp("Polar RZ");
for i = 1:length(polar_rz)/(fs*bit_dur)
  if polar_rz((i-1)*fs*bit_dur+1:i*fs*bit_dur) == one
    disp(1);
  else
    disp(0);
  endif
endfor

% modulation of polar manchester 
one = [ones(1, (fs/2)*bit_dur).*-3, ones(1,(fs/2)*bit_dur).*3];
zero = [ones(1, (fs/2)*bit_dur).*3, ones(1,(fs/2)*bit_dur).*-3];

for i = 1:length(bits)
  if bits(i) == 1
    manchester((i-1)*fs*bit_dur+1:i*fs*bit_dur) = one;
  else
    manchester((i-1)*fs*bit_dur+1:i*fs*bit_dur) = zero;
  endif
endfor

subplot(3,1,2);
plot(t, manchester, 'linewidth', 3);
ylim([-5,5]);
xlim([0,T]);
grid on;
title("Polor Manchester");

% demodulation Polar Manchester
disp("Manchester");
for i = 1:length(manchester)/(fs*bit_dur)
  if manchester((i-1)*fs*bit_dur+1:i*fs*bit_dur) == one
    disp(1);
  else
    disp(0);
  endif
endfor


% differential manchester

% added very soon