likes(wallace, cheese).
likes(grommit, cheese).
likes(wendolene, sheep).

friend(X, Y) :- \+(X = Y), likes(X, Z), likes(Y, Z).

main :- write('hello').

%-------------------------------------------------
next_to(california, nevada).
next_to(pennsylvania, ohio). 
next_to(ohia, california).

travel(A, C) :- next_to(A, B), next_to(B, C).

%-------------------------------------------------
food_type(velveeta, cheese).
food_type(ritz, cracker).
food_type(spam, meat).
food_type(sausage, meat).
food_type(jolt, soda).
food_type(twinkie, dessert).

flavor(sweet, dessert).
flavor(savory, meat).
flavor(savory, cheese).
flavor(sweet, soda).

food_flavor(X, Y) :- food_type(X, Z), flavor(Y, Z).

parent(albert, bob).
parent(bob, carl).
parent(bob, charlie).
	
get_grandchild :- parent(albert, B), parent(B, C),
	write('Alberts grandchild is '),
	write(C), nl.
	
get_grandparent :- parent(X, carl), parent(X, charlie),
	format('~w ~s grandparent ~n', [X, "is the"]).

what_grade(5) :- write('Go to kindergarten').
what_grade(6) :- write('Go to 1st Grade').
what_grade(Other) :-
	Grade is Other - 5,
	format('Go to Grade ~w', [Grade]).
	
%-------------------------------------------------
different(red, green). different(red, blue).
different(green, red). different(green, blue).
different(blue, red). different(blue, green).

coloring(Alabama, Mississippi, Georgia, Tennessee, Florida) :-
	different(Mississippi, Tennessee),
	different(Mississippi, Alabama),
	different(Alabama, Tennessee),
	different(Alabama, Mississippi),
	different(Alabama, Georgia),
	different(Alabama, Florida),
	different(Georgia, Florida),
	different(Georgia, Tennessee).
% coloring(Alabama, Mississippi, Georgia, Tennessee, Florida).
% Type 'a' to get all possible outcomes. 

%-------------------------------------------------
cat(lion).
cat(tiger).

dorothy(X, Y, Z) :- X = lion, Y = tiger, Z = bear.
twin_cats(X, Y) :- cat(X), cat(Y).


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


%--------------------Recursion-----------------------------
father(zeb, john_boy_sr).
father(john_boy_sr, john_boy_jr).

ancestor(X, Y) :-
father(X, Y).
ancestor(X, Z) :-
	father(X, Y), ancestor(Y, Z).


%---------------------Lists & Tuples----------------------------
my_tuple :- (1, B, 3) = (A, 2, C).
my_list :- [2, 2, 3] = [X, X, Z], write('equal').
[1,2,3] = [Head|Tail]. %Works for any list where len >= 1. 
[a, b, c] = [a|[Head|Tail]]. %Starting from index.
[a, b, c, d, e] = [_, _|[Head|_]]. %Grab the 3rd element.


%---------------------Lists & Math----------------------------
count(0, []).
count(Count, [Head|Tail]) :- count(TailCount, Tail), Count is TailCount + 1.

sum(0, []).
sum(Total, [Head|Tail]) :- sum(Sum, Tail), Total is Head + Sum.

average(Average, List) :- sum(Sum, List), count(Count, List), Average is Sum/Count.


%---------------------Using rules in both directions----------------------------
%The rule append(List1, List2, List3) is true if List3 is List1 + List2
append([tiny], [bubbles], What). %List building
append([dessert_topping], Who, [dessert_topping, floor_wax]). %Subtraction
append(One, Two, [apples, oranges, bananas]). %Computes possible splits

%Building our own version of append, called concatenate.
%concatenate([], [harry], What).
concatenate([], List, List). %True if 1st arg is a list and next two are the same.
concatenate([Head|Tail1], List, [Head|Tail2]) :-
	concatenate(Tail1, List, Tail2).


%________________________Day 2__________________________________________________________________________

%Find an implementation of a Fibonacci series.
%https://stackoverflow.com/a/44497503
fib_seq(0,[0]).                   % <- base case 1
fib_seq(1,[0,1]).                 % <- base case 2
fib_seq(N,Seq) :-
   N > 1,
   fib_seq_(N,SeqR,1,[1,0]),      % <- actual relation (all other cases)
   reverse(SeqR,Seq).             % <- reverse/2 from library(lists)

fib_seq_(N,Seq,N,Seq).
fib_seq_(N,Seq,N0,[B,A|Fs]) :-
   N > N0,
   N1 is N0+1,
   C is A+B,
   fib_seq_(N,Seq,N1,[C,B,A|Fs]). % <- tail recursion


%Reverse the elements of a list.


%Find the smalles element of a list.


%Sort the elements of a list. 


%------------------------Sudoku---------------------------------------------------
% fd_domain(List, LowerBound, UpperBound). %This is true if LB >= list items >= UB
% fd_all_different(List). %succeeds if all the elements in List are different.

valid([]).
valid([Head|Tail]) :-
	fd_all_different(Head),
	valid(Tail).
	   
sudoku(Puzzle, Solution) :-
	Solution = Puzzle,
	Puzzle = [S11, S12, S13, S14,
			  S21, S22, S23, S24,
		      S31, S32, S33, S34,
			  S41, S42, S43, S44],
	fd_domain(Puzzle, 1, 4),

	Row1 = [S11, S12, S13, S14],
	Row2 = [S21, S22, S23, S24],
	Row3 = [S31, S32, S33, S34],
	Row4 = [S41, S42, S43, S44],

	Col1 = [S11, S21, S31, S41],
	Col2 = [S12, S22, S32, S42],
	Col3 = [S13, S23, S33, S43],
	Col4 = [S14, S24, S34, S44],

	Square1 = [S11, S12, S21, S22],
	Square2 = [S13, S14, S23, S24],
	Square3 = [S31, S32, S41, S42],
	Square4 = [S33, S34, S43, S44].

	valid([Row1, Row2, Row3, Row4,
		   Col1, Col2, Col3, Col4,
		   Square1, Square2, Square3, Square4]).

	   
%------------------------Eight Queens---------------------------------------------------
/* A board has eight queens.
Each queen has a row from 1–8 and a column from 1–8.
No two queens can share the same row.
No two queens can share the same column.
No two queens can share the same diagonal (southwest to northeast).
No two queens can share the same diagonal (northwest to southeast). */


animal(dog).
animal(turtle).
warmblooded(dog).
mammal(X) :- animal(X), warmblooded(X).
