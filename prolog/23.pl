% Facts defining the family tree
parent(john, mary).
parent(john, mike).
parent(susan, mary).
parent(susan, mike).
parent(mary, tom).
parent(mike, alice).
parent(tom, bob).

% Rule to find siblings
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Rule to find grandparents
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).

% Rule to find ancestors
ancestor(A, D) :- parent(A, D).
ancestor(A, D) :- parent(P, D), ancestor(A, P).


%?- sibling(mary, mike).
%?- grandparent(john, bob).
%?- ancestor(john, bob).
