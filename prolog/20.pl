% Planets Database
planet(mercury, 0).
planet(venus,  0).
planet(earth,  1).
planet(mars,  2).
planet(jupiter, 79).
planet(saturn, 83).
planet(uranus, 27).
planet(neptune, 14).

% Rule to retrieve moon count for a given planet
moons(Name, Count) :- planet(Name, Count).

% Query example:
% ?- moons(saturn, Count).
