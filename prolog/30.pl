% Facts: defining parent relationships
parent(john, mary).
parent(mary, alice).
parent(alice, tom).

% Rule to define grandparent relationship based on parent relationship
grandparent(X, Z) :- 
    parent(X, Y),   % X is a parent of Y
    parent(Y, Z).   % Y is a parent of Z

% Example Queries:
% Query to find the grandparents of someone:
% ?- grandparent(X, tom).      % Who are the grandparents of Tom?
% ?- grandparent(john, Who).   % Who is John's grandchild?
