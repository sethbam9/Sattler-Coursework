
! CLASSES

IN: syntax

TUPLE: rectangle width height ;
TUPLE: circle radius ; 

: <rectangle> ( w h -- r ) rectangle boa ; 
: <circle> ( r -- c ) circle boa ;

GENERIC: area ( shape -- n ) 

USE: math.constants

M: rectangle area 
[ width>> ] [ height>> ] bi * ;
M: circle area 
radius>> sq pi * ;

GENERIC: perimeter ( shape -- n )

M: rectangle perimeter
[ width>> ] [ height>> ] bi + 2 * ;
M: circle perimeter 
radius>> 2 * pi * ;

TUPLE: triangle base height ;

: <triangle> ( b h -- t ) triangle boa ;

M: triangle area 
[ base>> ] [ height>> ] bi * 2 / ;

USE: math.functions
: hypotenuse ( x y -- z ) [ sq ] bi@ + sqrt ;

M: triangle perimeter 
[ base>> ] [ height>> ] bi [ + ] [ hypotenuse ] 2bi + ;

! Run: n1 n2 <object> method .
! E.g. 5 10 <triangle> perimeter .