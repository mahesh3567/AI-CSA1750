% Define the connections between nodes
connected(1, 7, 1).
connected(1, 8, 1).
connected(1, 3, 1).
connected(7, 4, 1).
connected(7, 20, 1).
connected(7, 17, 1).
connected(8, 6, 1).
connected(3, 9, 1).
connected(3, 12, 1).
connected(9, 19, 1).
connected(4, 42, 1).
connected(20, 28, 1).
connected(17, 10, 1).

% Define bidirectional connections
connected2(X, Y, D) :- connected(X, Y, D).
connected2(X, Y, D) :- connected(Y, X, D).

% Find the next node
next_node(Current, Next, Path) :-
    connected2(Current, Next, _),
    \+ member(Next, Path).

% Breadth-first search
breadth_first(Goal, Goal, _, [Goal]).
breadth_first(Start, Goal, Visited, [Start|Path]) :-
    findall(Next,
            (next_node(Start, Next, Visited)),
            NextNodes),
    append(Visited, [Start], NewVisited),
    breadth_first_helper(NextNodes, Goal, NewVisited, Path).

breadth_first_helper([], _, _, []).
breadth_first_helper([Next|Rest], Goal, Visited, [Next|Path]) :-
    (   breadth_first(Next, Goal, Visited, Path)
    ->  true
    ;   breadth_first_helper(Rest, Goal, Visited, Path)
    ).

% Example query
% ?- breadth_first(1, 10, [], Path).
