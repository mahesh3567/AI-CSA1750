% Database to store names and DOBs
:- dynamic name_dob/2.

% Add a new entry to the database
add_entry(Name, DOB) :-
    assertz(name_dob(Name, DOB)).

% Retrieve DOB for a given Name
retrieve_entry(Name, DOB) :-
    name_dob(Name, DOB).

% Display all entries
display_entries :-
    findall(Name-DOB, name_dob(Name, DOB), Entries),
    print_entries(Entries).

% Helper to print entries
print_entries([]).
print_entries([Name-DOB | T]) :-
    format('Name: ~w, DOB: ~w~n', [Name, DOB]),
    print_entries(T).

%?- add_entry('karthik', '1990-05-01').
%?- add_entry('surya', '1985-12-10').
%?- display_entries.