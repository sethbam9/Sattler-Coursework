"""CHAPTER 13"""

""" Exercise 2
You are given an unsorted array containing integers and another integer s. How can
you ﬁnd all pairs of numbers (a,b) where a and b are contained in the array, so
that a + b = s, in time O(n)? Write a program which does that using a hash table. """

""" Exercise 3
How could you ﬁnd the most common word in a text using a hash table? """

""" Exercise 4
How can you implement the union, intersection, and diﬀerence of two sets using
hash tables? """


"""CHAPTER 16"""

""" Exercise 1
How would you select one line in random from a ﬁle, without reading it all in
memory? That means that you do not know how many lines there are. You canuse
reservoir sampling, where the reservoir is of size one. That means that when you
read the ﬁrst line, you pick it with probability equal to 1. When you read the
second line, if it exists, you pick it with probability equal to 1/2, so line
1 and line 2 have equal probability of being selected. When you read the third
line, again if it exists, you pick it with probability equal to 1/3. That means
that lines 1 and 2 have 2/3 probability of being selected, which they share
equally, because we saw that each one of them had 1/2 probability of being
selected previously; so each of the three lines has 1/3 probability of being
selected. We continue in this way until the end of the ﬁle. Implement reservoir
sampling to pick a random line from a ﬁle. Note that this version of reservoir
sampling can be much smaller than the general one. """

""" Exercise 2
There are applications where we need to sample according to some predeﬁned
weights: that is, the probability that an item is sampled must be proportional
to its weight. This is called weighted sampling. We can do that with a variation
of reservoir sampling. We start by inserting the ﬁrst m items in the reservoir,
but we associate with each item i a key equal to u1/wi, where wi is its weight
and u is a random number selected uniformly in the range from 0 to 1 (included).
Then for each item k that follows, we get again a random number u in the
range[0, 1] and calculate its key u1/wk; if this is greater than the smallest
key in the reservoir, we insert the new item in the reservoir, replacing the one
with the smallest key. Implement this scheme using a minimum priority queue to
ﬁnd each time the item that has the smallest key in the reservoir. """
