clear all;
close all;
clc;

bits = [0 1 0 0 1 1 1 0];
bit_dur = 2;

fs = 100;
T = length(bits) * bit_dur;

t = 0:1/fs:T-(1/fs);

% NRZ-L
for i = 1:length(bits)
  if bits(i) == 0
    nrzl((i-1)*fs*bit_dur+1:i*fs*bit_dur) = -3;
  else
    nrzl((i-1)*fs*bit_dur+1:i*fs*bit_dur) = 3;
  endif
endfor

subplot(2,1,1);
plot(t,nrzl);
ylim([-5,5]);
xlim([0, T]);
grid on;
title("NRZ-L");
xlabel("Time");
ylabel("Amplitude");

% demodulation NRZ-L
for i = 1:length(nrzl)/(fs*bit_dur)
  if nrzl((i-1)*fs*bit_dur+1:i*fs*bit_dur) == ones(1, (fs*bit_dur)) .* -3
    disp(0);
  else
    disp(1);
  endif
endfor  


% NRZ-I if found 1-> transition
lastbit = 3;
for i = 1:length(bits)
  if bits(i) == 1
    nrzi((i-1)*fs*bit_dur+1:i*fs*bit_dur) = -lastbit;
    lastbit = -lastbit;
  else
    nrzi((i-1)*fs*bit_dur+1:i*fs*bit_dur) = lastbit;
  endif
endfor

subplot(2,1,2);
plot(t,nrzi);
ylim([-5,5]);
grid on;
title("NRZ-I");
xlabel("Time");
xlim([0, T]);
ylabel("Amplitude");

% demodulation NRZ-I
