% Define dynamic predicates
:- dynamic parent/2.
:- dynamic grandparent/2.

% Facts: defining parent relationships
parent(john, mary).
parent(mary, alice).
parent(alice, tom).

% Rule to define grandparent relationship based on parent relationship
forward_chain_grandparent :-
    parent(X, Y),              % Find parent X -> Y
    parent(Y, Z),              % Find parent Y -> Z
    \+ grandparent(X, Z),      % Ensure the grandparent fact doesn't already exist
    assert(grandparent(X, Z)),  % Assert new grandparent fact
    write('Inferred grandparent: '), write(X), write(' is the grandparent of '), writeln(Z),
    fail.                      % Force backtracking to find all possibilities

% The main predicate that runs forward chaining
run_forward_chaining :-
    (forward_chain_grandparent -> true; true),  % Execute forward chaining
    write('All forward chaining complete.'), nl. % Print completion message

% Example Queries:
% To run forward chaining and infer all grandparent relationships:
% ?- run_forward_chaining.
