% Define the sum predicate
sum(0, 0).  % Base case: sum from 1 to 0 is 0
sum(N, Sum) :- Sum is N*(N+1) / 2.
% ?- sum(5, Sum).
