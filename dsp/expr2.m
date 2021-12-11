% x = input("Enter the first sequence: ");
% h = input("Enter the second seqence: ");

x = [1 2 3 4]
h = [1 1 1 1]

y = conv(x,h)

subplot(3,1,1)
stem(x);
title("Input Sequence")

subplot(3,1,2)
stem(h);
title("Impulse Sequence")

subplot(3,1,3)
stem(y);
title("After convolution Sequence")


