% Facts about bird species and their characteristics
bird(pigeon, small, grey, true).
bird(eagle, large, brown, true).
bird(ostrich, large, black_and_white, false).
bird(penguin, small, black_and_white, false).
bird(sparrow, small, brown, true).

% Predicate to check if a bird can fly
can_fly(Bird) :-
    bird(Bird, _, _, true),
    write(Bird), write(' can fly.'), nl.

can_fly(Bird) :-
    bird(Bird, _, _, false),
    write(Bird), write(' cannot fly.'), nl.
% Example queries
%?- can_fly(pigeon).

