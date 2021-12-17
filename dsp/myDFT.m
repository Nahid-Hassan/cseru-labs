function X=myDFT(x,N)
L = length(x);

if N < L
  error('N must be greater than or equal to length of x');
endif

x = [x zeros(1, N-L)];
X = zeros(1, N);

for m=0:N-1
  for n=0:N-1
    X(m+1) = X(m+1) + x(n+1) * exp(-j*2*pi*m*n/N); % X(m+1)-> m+1 because matlab use 1-based indexing.
  endfor
endfor
  
endfunction
