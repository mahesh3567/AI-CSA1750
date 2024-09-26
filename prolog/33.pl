is_vowel(Char) :- member(Char, ['a', 'e', 'i', 'o', 'u']).

count_vowels([], 0).
count_vowels([H|T], Count) :-
    is_vowel(H),
    count_vowels(T, TailCount),
    Count is TailCount + 1.
count_vowels([H|T], Count) :-
    \+ is_vowel(H),
    count_vowels(T, Count).

vowel_count(String, Count) :-
    string_chars(String, Chars),
    count_vowels(Chars, Count).


%?- vowel_count("aim", Count).	
