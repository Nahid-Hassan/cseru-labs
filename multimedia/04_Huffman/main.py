# A Huffman Tree Node
import heapq
from collections import Counter


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""

    def __lt__(self, nxt):
        return self.freq < nxt.freq


output = open("output.txt", "w")
encode_dict, decode_dict = {}, {}


def printNodes(node, val=""):
    newVal = val + str(node.huff)

    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)

    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")
        output.write(f"{node.symbol} -> {newVal}" + "\n")
        encode_dict[node.symbol] = newVal
        decode_dict[newVal] = node.symbol


def encode(msg):
    for key, val in encode_dict.items():
        msg = msg.replace(key, val)
    return msg


def decode(msg):
    for key, val in decode_dict.items():
        msg = msg.replace(key, val)
    return msg


with open("input.txt", "r") as f:
    lines = f.readlines()

nodes = []
for key, val in Counter(lines[0]).items():
    heapq.heappush(nodes, node(val / len(lines[0]), key))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.huff = 0
    right.huff = 1

    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newNode)

printNodes(nodes[0])

out = encode(lines[0])
open("encode.txt", "w").write(out)
# print(f"After compressed string -> {lines[0]} - {out}.")
inp = open("encode.txt", "r").readlines()[0]
open("decode.txt", "w").write( decode(inp) )
# print(f"After decompressing string -> {out} - {decode(out)}.")
