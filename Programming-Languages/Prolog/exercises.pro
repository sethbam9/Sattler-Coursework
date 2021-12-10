%________________________Day 1__________________________________________________________________________

author_of(tolkien, 'Lord of the Rings').
author_of(tolkien, 'The Hobbit').
author_of(tolkien, 'The Silmarillion'). 
author_of(tolkien, 'The Children of Hurin'). 
author_of(twain, 'Huckleberry Finn').
author_of(chan, 'Crazy Love'). 

authored(X, Y) :- author_of(X, Y).

%--------------------
plays(john, guitar).
plays(jill, violin). 
plays(ahmed, guitar).
plays(chad, drums). 
plays(ron, bass).

genre(john, folk).
genre(jill, classical). 
genre(ahmed, indie).
genre(chad, regge). 
genre(ron, rock). 

plays_instrument(X, Y) :- plays(X, Y). 
plays_instrument(X,Y) :- plays(X, Z), genre(Y, Z).


%________________________Day 2__________________________________________________________________________
/* All my code from day 2 is from
	https://github.com/nickknw/seven-languages-in-seven-weeks/blob/master/week-3-prolog/day2.pl
I spent hours researching, but the language just does not makes sense to me. 
*/

%Reverse the elementS of a list.
reverse(A,R) :- reverse(A,[],R).
reverse([X|Y],Z,W) :- reverse(Y,[X|Z],W).
reverse([],X,X).
	
%Find the smallest element of a list.
min(A,A,A).
min(A,B,B) :- B < A.
min(A,B,A) :- A < B.

minInList([X|XS], M) :- minInList(XS, M1), min(X, M1, M).
minInList([X], X).

%Sort the elements of a list. 
takeout(X, [X|R], R).
takeout(X, [F|R], [F|S]) :- takeout(X,R,S).

mySort(List, [Min|Sorted]) :- 
   minInList(List, Min), 
   takeout(Min, List, Rest), 
   mySort(Rest, Sorted).
mySort([X], [X]).

%________________________Day 3__________________________________________________________________________

valid([]).
valid([Head|Tail]) :-
	fd_all_different(Head),
	valid(Tail).
	   
sudoku(Puzzle, Solution) :-
	Solution = Puzzle,
	Puzzle = [S11, S12, S13, S14, S15, S16,
			  S21, S22, S23, S24, S25, S26,
			  S31, S32, S33, S34, S35, S36,
			  S41, S42, S43, S44, S45, S46,
			  S51, S52, S53, S54, S55, S56,
			  S61, S62, S63, S64, S65, S66],
	fd_domain(Puzzle, 1, 6),

	Row1 = [S11, S12, S13, S14, S15, S16],
	Row2 = [S21, S22, S23, S24, S25, S26],
	Row3 = [S31, S32, S33, S34, S35, S36],
	Row4 = [S41, S42, S43, S44, S45, S46],
	Row5 = [S51, S52, S53, S54, S55, S56],
	Row6 = [S61, S62, S63, S64, S65, S66],

	Col1 = [S11, S12, S13, S14, S15, S16],
	Col2 = [S21, S22, S23, S24, S25, S26],
	Col3 = [S31, S32, S33, S34, S35, S36],
	Col4 = [S41, S42, S43, S44, S45, S46],
	Col5 = [S51, S52, S53, S54, S55, S56],
	Col6 = [S61, S62, S63, S64, S65, S66],

	Square1 = [S11, S12, S13, S14, S15, S16],
	Square2 = [S21, S22, S23, S24, S25, S26],
	Square3 = [S31, S32, S33, S34, S35, S36],
	Square4 = [S41, S42, S43, S44, S45, S46],
	Square5 = [S51, S52, S53, S54, S55, S56],
	Square6 = [S61, S62, S63, S64, S65, S66],

	valid([Row1, Row2, Row3, Row4, Row5, Row6,
		   Col1, Col2, Col3, Col4, Col5, Col6,
		   Square1, Square2, Square3, Square4, Square5, Square6]).
		   
/* 
sudoku([2, 6, _, 5, _, 1,
_, _, 1, _, _, 2,
4, _, _, _, 6, _,
_, 3, _, _, _, 4,
1, _, _, 4, _, _,
3, _, 4, _, 2, 6], 
Solution).

sudoku([
_, 1, _, _, 5, 3,
2, _, 3, 1, 6, _,
_, _, 2, 6, _, _,
5, 6, _, 3, _, _,
6, 2, 5, 4, _, _,
_, _, 1, _, 2, 6], 
Solution).
*/
