%Unit Step Sequence:

N = 21;
n = 0:1:N-1;
x = ones(1, N);
subplot(2, 2, 1);
stem(n, x);
xlabel('n');
ylabel('x(n)');
title('Unit Step Sequence'); 