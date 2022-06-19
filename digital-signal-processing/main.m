clear all;
close all;
clc;

% X(m) = summation(0, N-1) x(n) e ^ (-j2pimn/N)

x = 1:8

N = length(x);
X = myDFT(x,N);

fr = linspace(0,N);
stem(N,abs(X));
