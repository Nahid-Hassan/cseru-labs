from decimal import Decimal, getcontext
from collections import Counter

# Set decimal precision
getcontext().prec = 30

def generate_probability_range(symbols):
    total_count = len(symbols)
    symbol_count = Counter(symbols)
    prob_range = {}
    low = Decimal(0) 
    for symbol, count in symbol_count.items():
        prob = Decimal(count) / Decimal(total_count)
        high = low + prob
        prob_range[symbol] = (low, high)
        #print(symbol,prob_range[symbol])
        low = high
    print(prob_range)
    return prob_range

def encode(symbols, prob_range):
    low = Decimal(0)
    high = Decimal(1)
    for symbol in symbols:
        symbol_low, symbol_high = prob_range[symbol]
        range_width = high - low
        high = low + range_width * symbol_high
        low = low + range_width * symbol_low
    return (low, high)

def decode(encoded_message, prob_range, message_length):
    low, high = encoded_message
    message = ""
    print(prob_range.items())
    for i in range(message_length):
        for symbol, symbol_range in prob_range.items():
            symbol_low, symbol_high = symbol_range
            symbol_width = symbol_high - symbol_low
            if low >= symbol_low and high <= symbol_high:
                message += symbol
                high = (high - symbol_low) / symbol_width
                low = (low - symbol_low) / symbol_width
                break
    return message

# Read input from file
with open("input.txt", "r") as f:
    input_string = f.read().strip()

# Generate probability range
prob_range = generate_probability_range(input_string)

# Encode input string
encoded_message = encode(input_string, prob_range)

# Decode encoded message
decoded_message = decode(encoded_message, prob_range, len(input_string))

# Write encoded message to file
with open("encoded_output.txt", "w") as f:
    f.write(str(encoded_message))

# Write decoded message to file
with open("decoded_output.txt", "w") as f:
    f.write(decoded_message)
