from heapq import heappush, heappop, heapify
from collections import defaultdict


def huffman_encode(data):
    # Step 1: Calculate the frequency of each character in the data
    freq = defaultdict(int)
    for c in data:
        freq[c] += 1

    # Step 2: Create a priority queue of nodes
    heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
    heapify(heap)

    # Step 3: Combine the two nodes with the lowest frequency into a new node
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Step 4: Generate the Huffman codes for each character
    huffman_code = dict(heappop(heap)[1:])
    return {symbol: huffman_code[symbol] for symbol in freq.keys()}


def huffman_decode(data, codes):
    # Step 1: Invert the codes dictionary
    inverted_codes = {code: symbol for symbol, code in codes.items()}

    # Step 2: Decode the data using the inverted codes dictionary
    result = ""
    code = ""
    for bit in data:
        code += bit
        if code in inverted_codes:
            symbol = inverted_codes[code]
            result += symbol
            code = ""
    return result


original_data = "hello world"
codes = huffman_encode(original_data)
encoded_data = ''.join([codes[c] for c in original_data])
decoded_data = huffman_decode(encoded_data, codes)
print(original_data == decoded_data)  # True
