#!/usr/bin/perl

use 5.010;
use strict;
use warnings;
# Three types of variables: SCALARS (things), ARRAYS (lists), and HASHES (dictionaries)

# SCALARS
my $number = 20;
my $string = "apples";
my $date = '09/14/2020_$"@"\\';
print "$date,\nHello friend,\n\tI bought $number $string.\nHow many did you buy?\n\n";
my $str = "\Uname\E\t\uage\t\LweIght\E\n";
print $str;

# concatination 
my $concat = "he" . "llo" . " THERE";
print $concat, "\n";
$concat .= "!\n";
print $concat;
# uc( $str ) is uppercase
# lc( $str ) is lowercase
# length($str) is length

# extracting & locating substrings:
print substr("hello there", 6), "\n"; # there
print substr("hello there", 6, 3), "\n"; # the
my $ind = index($concat, "e");
print $ind, "\n";
# replicating a string:
print 'ab.' x 5, "\n\n";
# ARRAYS
my @num_array = (1..6);  
my @str_array = qw/a b c d e f/;
my $i = 0;
my $ord_num;
	if($i == 0){
		$ord_num = "st";
	}elsif($i == 1){
		$ord_num = "nd";
	}elsif($i == 2){
		$ord_num = "rd";
	}else{
		$ord_num = "th";
}
print "The ", $num_array[$i], "$ord_num letter 
in the alphabet is ", "'", $str_array[$i], "'.\n"; 
print "Length of array: $#num_array\n\n";

#autovivification:
my @arr = qw{0 10 fire};
$arr[6] = "ice" ; #(N
print "@arr\n"; #01 two 6 #(0
my $size = @arr; #(P
print "$size\n";

#insert sliced array into another
my @barr = ("hi", "hi");my @carr = (@barr, @arr[0,2]); 
print "@carr\n";

# HASHES
my %h = ('a', 1, 'b', 2, 'c', 3); 
my %h2 = (a => 1,
	b => 2,
	c => 3,
	d => 4);
#&display_hash( \%h );
print %h2, "\n";


# LEXICAL VARIABLES
my ($x, @arr, %phone_list) ; # declaring multiple variables at once. 
$x = 4;
@arr = (1, 2, 3, "four");
%phone_list = ( peter => 123, paul => 234, mary => 345 ) ;

# Creating SUBROUTINES (functions): sub function_name { . . . }# Function call: function_name()
sub Hello {
   print "Hello, World!\n";
}
Hello();
package StringJoiner; #(A)
sub wordjoiner { #(B)
	my $self = shift; #(C)
	my $joinedwords = ""; #(D)
	foreach ( @$self ) { #(E)
		$joinedwords .= $_; #(F)
	}
	$joinedwords; #(G)
}


# CLASSES
class Dog {
	name;
	color;
	
	bark() {
		print "woof woof";
	}
	growl() {
		print "grrr";
	}
}
growl();
bark();