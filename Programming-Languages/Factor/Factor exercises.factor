! DAY 1 EXERCISES (EASY): . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

! Using only * and +, how would you calculate 3^2 + 4^2 with Factor?
3 3 * 4 4 * + .

! Enter USE: math.functions in the Listener. Now, with sq and sqrt, calculate the
! square root of 3^2 + 4^2.
USE: math.functions
3 sq 4 sq + sqrt .

! If you had the numbers 1 2 on the stack, what code could you use to end
! up with 1 1 2 on the stack?
1 2
1 swap

! Enter USE: ascii in the Listener. Put your name on the stack, and write a
! line of code that puts "Hello, " in front of your name and converts the whole
! string to uppercase. Use the append word to concatenate two strings and
! >upper to convert to uppercase. Did you have to do any stack shuffling to
! get the desired result?
USE: ascii
"Seth"
"Hello, " swap append >upper



! DAY 2 EXERCISES (EASY): . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

! Create an examples.strings vocabulary and write a word named palindrome?
! that takes a string from the stack and returns t or f according to whether
! or not the word is a palindrome (a word that is spelled the same frontward
! and backward, such as racecar).
! SEE: https://andreaferretti.github.io/factor-tutorial/. 
USE: tools.scaffold
"examples.strings" scaffold-work

USING: ;
IN: examples.strings

: palindrome? ( str -- bool ) dup reverse equal? ;


! In the appropriate vocabulary for associating tests with the examples.strings
! vocabulary, write two unit tests for palindrome?, one that expects t and one
! that expects f.
USING: examples.strings tools.test ;
IN: examples.greeter.tests 

{ f } [ "river" palindrome? . ] unit-test
{ t } [ "mom" palindrome? . ] unit-test


! Add the examples.strings to the test suite so that its tests are included when
! running test-suite.factor.


! DAY 3 EXERCISES (EASY): . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

! Define a constructor for cart-item that accepts a price and returns a cart-item
! with a default name and quantity.
TUPLE: cart-item name price quantity ;
: <my-cart-item> ( price -- cart-item ) 1 "Computer" cart-item boa ;
: <computer-cart-item> ( price -- cart-item ) T{ cart-item { name "Computer" } { quantity 1 } { price price } } ;

600.00 <my-cart-item> .

! Write a word that discounts the price of a cart-item by a percentage that is
! given as a parameter.
