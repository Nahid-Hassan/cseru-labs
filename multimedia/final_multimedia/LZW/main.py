def lzw_encode(data):
    dictionary = {chr(i): i for i in range(256)}
    result = []
    w = ""
    for c in data:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = len(dictionary)
            w = c
    if w:
        result.append(dictionary[w])
    return result


def lzw_decode(data):
    dictionary = {i: chr(i) for i in range(256)}
    result = ""
    w = chr(data.pop(0))
    result += w
    for k in data:
        if k in dictionary:
            entry = dictionary[k]
        elif k == len(dictionary):
            entry = w + w[0]
        else:
            raise ValueError("Bad compressed k: %s" % k)
        result += entry
        dictionary[len(dictionary)] = w + entry[0]
        w = entry
    return result


original_data = "hello world"
encoded_data = lzw_encode(original_data)
decoded_data = lzw_decode(encoded_data)
print(original_data == decoded_data)  # True
