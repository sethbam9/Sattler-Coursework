"""CHAPTER 3"""

""" Exercise 2
Implement a minimum and a maximum priority queue using an array with the convention
described in the text: the element at position 0 will be the minimum, or maximum,
and for each node i its left child will be at position 2i + 1 and its right child
at position 2i + 2. Try to design your code so that you reuse as much as possible
so that both the minimum and maximum priority queue implementations share as much
code as possible. """

""" Exercise 4
We have described how Huﬀman codes are built, but we have not gone into the details
of how they can be programmed in a computer. Before we can call algorithm 3.1, we
need to go through the text to be encoded and do the frequency counts for the
characters in the text. After algorithm 3.1 has completed, we can create a table
like the one in table 3.7, which we use to encode each character in the text with
its Huﬀman encoding. The compressed output, usually a ﬁle, must contain two things:
the table we have created and the actual encoded text. We need the table, otherwise
we will not know how to decode the text in the future. The encoded text consists
of a series of bits not characters. Taking table 3.7 again, you should not output
the string "1110" for V, but the four digits 1, 1, 1, 0. This may not be
straightforward, as many programming languages output bytes by default, so that you
need to pack the bits into the bytes that will be output. With all these, you can
write your own Huﬀman encoder and decoder. """

""" Exercise 5
Using a Huﬀman encoder, encode a substantial amount of English text and check how
close the length of the encodings for each letter are to the encodings used by the
Morse code. """
"""SEVERAL SENTENCES: generate the huffman code & then compress it -> give it text
so that it generates the huffman code & then compress that.
It should look pretty similar to the Morse code. """
# Algorithm 3.1: Huﬀman code creation. Pg. 71
def createHuffmanCode(pq):
    while len(pq) > 1:
        x = min(pq)
        pq.remove(x)
        y = min(pq)
        pq.remove(y)
        sum = x + y
        z = createTree(sum, x, y)
        pq.append(z)
    return min(pq)

from anytree import Node, RenderTree #https://pypi.org/project/anytree/
def createTree(d, x, y):
    top = Node(d)
    left = Node(x, parent=top)
    right = Node(y, parent=top)
    return RenderTree(top)

""" Exercise 7
We have described LZW decompression using a decoding table. However, this table
maps from numerical values to strings, so we could use an array of strings instead.
Rewrite and implement algorithm 3.5 using an array for the decoding table dt. """

# Algorithm 3.5: LZW decompression. Pg. 88
def LZWDecompress(compressed, n_bits, n_items):
    max_code = (2 ** n_bits)
    dt = [] #dt: decoding table
    for i in range(n_items):
        dt.append(i)
    code = n_items
    decompressed = ""
    c = compressed[0]
    compressed.remove(c)
    v = dt[c]
    decompressed += v
    pv = v
    for c in compressed:
        v = dt[c]
        if v == None:
            v = pv + pv[0]
        decompressed += v
        if code <= max_code:
            insertInMap(dt, code, pv + v[0])
            code += 1
        pv = v
    return decompressed
