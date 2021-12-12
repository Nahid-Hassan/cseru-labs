%Unit Step Sequence:
N = 21;
n = 0:1:N-1;
x = ones(1, N);
subplot(3, 2, 1);
stem(n, x);
xlabel('n');
ylabel('x(n)');
title('Unit Step Sequence'); 

%Exponential sequence:
x2 = 0.8.^(n);
%plot(2);
subplot(3, 2, 2);
stem(n, x2);
xlabel('n');
ylabel('x(n)');
title('Exponential Sequence');

%Ramp Sequence 
x = input('Enter the length of ramp sequence: ');
t = 0:x;
subplot(3, 2, 3);
stem(t,t);
xlabel('c');
ylabel('Apmplitude');
title('Ramp Sequence');

% Exponential Sequence:-
N = input('Enter the no of points: ');
n = 0:.5:N-1;
x = 2.^(n);
subplot(3, 2, 4);
stem(n, x);
xlabel('n');
ylabel('x(n)');
title('Exponential Sequence');

% Sinusoidal Sequence:
t = 0:0.01:pi;
y = sin(2*pi*t);
subplot(3, 2, 5);
%stem(t, y);
plot(t, y);
xlabel('e');
ylabel('Amplitude');
title('Sinusoidal Sequence');

% Cosine Sequence:
t = 0:0.01:pi;
y = cos(2*pi*t);
subplot(3, 2, 6);
plot(t, y);
xlabel('f');
ylabel('Amplitude');
title('Cosine Sequence');