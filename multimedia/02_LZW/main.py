# input: BABAABAAA
"""
     65  - A
     66  - B
66 - 256 - BA
65 - 257 - AB
256 
"""
def lzw_compress(data):
    d = {chr(i): i for i in range(256)}
    next_code = 256
    compressed = []
    cs = ""                             # current sequence
    
    # BABAA
    for symbol in data:
        ns = cs + symbol                # new sequence
        if ns in d:                      
            cs = ns
        else:
            compressed.append(d[cs])
            d[ns] = next_code
            next_code += 1
            cs = symbol
    
    if cs in d:
        compressed.append(d[cs])
    
    # print(compressed)
    return compressed


def lzw_decompress(compressed):
    d = {i: chr(i) for i in range(256)}
    next_code = 256
    decompressed = ""
    ps = chr(compressed[0])
    decompressed += ps
    
    # 66 65 256 65
    for code in compressed[1:]:
        if code in d:
            cs = d[code]
        elif code == next_code:
            cs = ps + ps[0]
            print(cs, '----------------')
        else:
            raise ValueError("Invalid compressed code")
        
        decompressed += cs
        # print(code, cs, decompressed)
        d[next_code] = ps + cs[0]
        next_code += 1
        ps = cs
    
    return decompressed


# Read input from file
with open('input.txt', 'r') as file:
    input_data = file.read().rstrip()

# Compress the data
compressed_data = lzw_compress(input_data)

# Write compressed data to file
with open('compressed.txt', 'w') as file:
    file.write(' '.join(map(str, compressed_data)))

# Read compressed data from file
with open('compressed.txt', 'r') as file:
    compressed_data = list(map(int, file.read().split()))

# Decompress the data
decompressed_data = lzw_decompress(compressed_data)

# Write decompressed data to file
with open('decompressed.txt', 'w') as file:
    file.write(decompressed_data)

# print(len(compressed_data) / len(input_data))
