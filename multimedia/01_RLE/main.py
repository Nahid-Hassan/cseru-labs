import itertools


def rle_encode(data):
    encoded = ""
    prev_char = data[0]
    count = 1

    # aaabaa
    for char in data[1:]:
        if prev_char == char:
            count += 1
        else:
            encoded += str(count) + prev_char
            prev_char = char
            count = 1
    
    encoded += str(count) + prev_char
    return encoded


def rle_decode(data):
    decoded = ""
    i = 0
    while i < len(data):
        count_str = ""
        # 40a2c
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        count = int(count_str)
        decoded += data[i] * count
        i += 1
    return decoded


encoded_data = []
with open("plain.txt", "r") as file:
    for line in file.readlines():
        encoded_data.append(rle_encode(line.rstrip()))

with open("encoded.txt", "w") as file:
    for line in encoded_data:
        file.write(line + "\n")

decoded_data = []
with open("encoded.txt", "r") as file:
    for line in file.readlines():
        decoded_data.append(rle_decode(line.rstrip()))

with open("decoded.txt", "w") as file:
    for line in decoded_data:
        file.write(line + "\n")
