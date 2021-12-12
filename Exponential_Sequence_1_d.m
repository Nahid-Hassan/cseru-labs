% Exponential Sequence:-

N = input('Enter the no of points: ');
n = 0:.5:N-1;
x = 2.^(n);
stem(n, x);
xlabel('n');
ylabel('x(n)');
title('Exponential Sequence');
