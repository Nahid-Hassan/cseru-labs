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

xx = open("output.txt", "w")

encode_dict, decode_dict = {}, {}

def printNodes(node, val=""):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)

    if not node.left and not node.right:
        xx.write(f"{node.symbol} -> {newVal}" + "\n")
        encode_dict[node.symbol] = newVal
        decode_dict[newVal] = node.symbol


def encode(msg):
    for key, val in encode_dict.items():
        msg = msg.replace(key, val)
    return msg

def decode(msg):
    for key, val in decode_dict.items():
        msg = msg.replace(val, key)
        print(key, val, msg)
    return msg


with open("input.txt", "r") as f:
    lines = f.readlines();

nodes = []
for key, val in Counter(lines[0]).items():
    heapq.heappush(nodes, node(val, key))



# chars = ["a", "b", "c", "d", "e", "f"]
# freq = [5, 9, 12, 13, 16, 45]

# nodes = []
# for x in range(len(chars)):
#     heapq.heappush(nodes, node(freq[x], chars[x]))

# nodes[o3, o4, o5, o6]

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
print(out)
xx.write(out + "\n")
print(decode(out))