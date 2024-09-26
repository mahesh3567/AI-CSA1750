% Define the move transitions
move(state(door, not_taken), pick_up_banana, state(door, taken)).
move(state(room, not_taken), pull_switch, state(room, taken)).
move(state(room, taken), drop_banana, state(room, not_taken)).
move(state(door, taken), walk(room), state(room, taken)).
move(state(room, taken), walk(door), state(door, taken)).

% Define the goal condition
canget(state(_, taken)).
canget(State) :-
    move(State, _, NextState),
    canget(NextState).

% Example query
% ?- canget(state(door, not_taken)).