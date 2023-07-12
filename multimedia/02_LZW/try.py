def encode(data):
    d = {chr(i) : i for i in range(256)}
    compressed = []
    next_code = 256
    cs = ""

    for c in data:
        ns = cs + c

        if ns in d:
            cs = ns
        else:
            compressed.append(d[cs])
            d[ns] = next_code
            next_code += 1
            cs = c
    
    if cs in d:
        compressed.append(d[cs])
    return compressed

def decode(data):
    d = {i : chr(i) for i in range(256)}
    decompressed = ""
    next_code = 256
    ps = chr(data[0])
    decompressed += ps

    for code in data[1:]:
        if code in d:
            cs = d[code]
        elif code == next_code:
            cs = ps + ps[0]
        
        decompressed += cs
        d[next_code] = ps + cs[0]
        next_code += 1
        ps = cs
    
    return decompressed