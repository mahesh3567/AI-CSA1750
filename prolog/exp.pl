:- dynamic name_dob/2.

name_dob('karthik', '1990-05-01').
name_dob('surya', '1985-12-10').

display_entries :-
    findall(Name-DOB, name_dob(Name, DOB), Entries),
    print_entries(Entries).

print_entries([]).
print_entries([Name-DOB | T]) :-
    format('Name: ~w, DOB: ~w~n', [Name, DOB]),
    print_entries(T).

display_entries.