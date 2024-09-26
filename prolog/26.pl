% Facts
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(lemon, yellow).

% Rule to find color
find_color(Fruit, Color) :-
    fruit_color(Fruit, Color).
%?- find_color(apple, Color).
