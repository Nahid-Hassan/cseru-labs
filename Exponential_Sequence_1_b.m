%Exponential sequence:

N = 21;
n = 0:1:N-1;
x2 = 0.8.^(n);
%plot(2);
stem(n, x2);
xlabel('n');
ylabel('x(n)');
title('Exponential Sequence');