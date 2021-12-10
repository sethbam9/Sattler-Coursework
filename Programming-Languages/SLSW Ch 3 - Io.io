
# In shell:
cd OneDrive\Desktop\Sattler College\6. Spring 2021\CS 303 Programming Languages\iobin-win32-current\IoLanguage\bin
io_static
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" # Day 1 Challenge, p. 56 """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Evaluate 1 + 1 and then 1 + "one". Is Io strongly typed or weakly typed?
1 + 1 # -> 2
1 + "one" # Error: must be num, not sequence. (Strongly typed)

# Is 0 true or false? What about the empty string? Is nil true or false?
0 true # -> true
"" # -> true
nil true # -> true

# How can you tell what slots a prototype supports?

# What is the difference between = (equals), := (colon equals),
# and ::= (colon colon equals)? When would you use each one?
a ::= 1
b := 2
a = a + 1

# Run an Io program from a file:
io_static intro.io
doFile("intro.io") # from within static_io

# Execute the code in a slot given its name.
slot := Object clone


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" # Day 2 Challenge, p. 64 """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 1. A Fibonacci sequence starts with two 1s. Each subsequent number is
# the sum of the two numbers that came before: 1, 1, 2, 3, 5, 8, 13, 21,
# and so on. Write a program to find the nth Fibonacci number. fib(1) is
# 1, and fib(4) is 3.
fib := method(n,
  if(n <= 2, return 1,
    a := 0;
    b := 1;
    for(i, 2, n,
      c := a + b;
      a = b;
      b = c
    )
    return c
  )
)

# As a bonus, solve the problem with recursion and with loops.
# https://github.com/IoLanguage/io/blob/master/samples/shootout/recursive.io
fib := method(n,
  if(n <= 2, return 1)
  return fib(n - 1) + fib(n - 2)
)

# 2. How would you change / to return 0 if the denominator is zero?

# 3. Write a program to add up all of the numbers in a two-dimensional array.
array_sum := method(array,
  sum := 0;
  for(i, 0, array size - 1,
    sum = sum + array at(i)
  )
  return sum
)

# Using foreach
array_sum := method(array,
  array foreach(i, v, v = v + array at(i))
)

# 4. Add a slot called myAverage to a list that computes the average of all the
# numbers in a list. What happens if there are no numbers in a list?
# (Bonus: Raise an Io exception if any item in the list is not a number.)
my_list := list(18,21,28,30,24)

List myAverage := method(l,
  # sum := l foreach(i, v, v = v + l at(i));
  sum := 0;
  for(i, 0, l size - 1,
    sum = sum + l at(i)
  )
  return sum / l size
)

List myAverage(my_list)

# 5. Write a prototype for a two-dimensional list. The dim(x, y) method should
# allocate a list of y lists that are x elements long. set(x, y, value) should set
# a value, and get(x, y) should return that value.

# 6. Bonus: Write a transpose method so that (new_matrix get(y, x)) == matrix
# get(x, y) on the original list.

# 7. Write the matrix to a file, and read a matrix from a file.

# 8. Write a program that gives you ten tries to guess a random number from 1–100.
# If you would like, give a hint of “hotter” or “colder” after the first guess.


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""" # Day 3 Challenge, p. 73 """
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Enhance the XML program to add spaces to show the indentation structure.


# Create a list syntax that uses brackets.


# Enhance the XML program to handle attributes: if the first argument is
# a map (use the curly brackets syntax), add attributes to the XML program.
# For example: book({"author": "Tate"}...) would print <book author="Tate">:









# **********************************************************************
# Notes
# **********************************************************************
method("So, you've come for an argument." println)

# Lists
toDos := list("find my car", "find Continuum Transfunctioner")
toDos append("Find a present")
list(1, 2, 3, 4) average
list(1, 2, 3) at(1)
list(1, 2, 3) append(4)
list() isEmpty

# Maps
elvis := Map clone
elvis atPut("home", "Graceland")
elvis at("home")

# Boolean
true and false
4 < 5 and 6 > 7

# Loops
loop("getting dizzy..." println) #infinit
i := 1
while(i <= 11, i println; i = i + 1); "This one goes up to 11" println
for(i, 1, 11, i println); "This one goes up to 11" println
# if(condition, true code, false code)
if(false) then("It is true." println) else("It is false." println)
if_then := method(y,
if(y < 10)
then(
x := y;
)
else(
x := 2;
)
return x
)

# Messages
postOffice := Object clone
postOffice packageSender := method(call sender)
mailer := Object clone
mailer deliver := method(postOffice packageSender)
postOffice messageTarget := method(call target)

# Use msg to implement unless
unless := method(
(call sender doMessage(call message argAt(0))) ifFalse(
call sender doMessage(call message argAt(1))) ifTrue(
call sender doMessage(call message argAt(2)))
)
unless(1 == 2, write("One is not two\n"), write("one is two\n"))
.. to append e.g. "Ab".."e" is Abe

Object ancestors := method(
  prototype := self proto
  if(prototype != Object,
  writeln("Slots of ", prototype type, "\n---------------")
  prototype slotNames foreach(slotName, writeln(slotName))
  writeln
  prototype ancestors))
Animal := Object clone
Animal speak := method(
  "ambiguous animal noise" println)
Duck := Animal clone
Duck speak := method(
  "quack" println)
Duck walk := method(
  "waddle" println)
disco := Duck clone
disco ancestors

# TEXT INPUT
who := method(
  "What is your name?" println;
  x := File standardInput readLine;
writeln("Hi ", x)
)
