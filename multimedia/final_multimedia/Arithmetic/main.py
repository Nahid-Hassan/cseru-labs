from collections import Counter
import numpy as np

class ArithmeticEncoder:
    def __init__(self, symbols):
        self.symbols = symbols
        self.cumulative_freqs = self.calculate_cumulative_frequencies(symbols)
        
    def calculate_cumulative_frequencies(self, symbols):
        freqs = Counter(symbols)
        cumulative_freqs = {}
        current_sum = 0
        for symbol, freq in sorted(freqs.items()):
            cumulative_freqs[symbol] = current_sum
            current_sum += freq
        return cumulative_freqs
    
    def encode(self, data):
        low = 0
        high = 1
        for symbol in data:
            symbol_range = high - low
            symbol_low = low + symbol_range * self.cumulative_freqs[symbol] / len(data)
            symbol_high = low + symbol_range * (self.cumulative_freqs[symbol] + 1) / len(data)
            low = symbol_low
            high = symbol_high
        return (low + high) / 2
    
class ArithmeticDecoder:
    def __init__(self, symbols, encoded_data):
        self.symbols = symbols
        self.cumulative_freqs = self.calculate_cumulative_frequencies(symbols)
        self.encoded_data = encoded_data
        
    def calculate_cumulative_frequencies(self, symbols):
        freqs = Counter(symbols)
        cumulative_freqs = {}
        current_sum = 0
        for symbol, freq in sorted(freqs.items()):
            cumulative_freqs[symbol] = current_sum
            current_sum += freq
        return cumulative_freqs
    
    def decode(self, length):
        low = 0
        high = 1
        data = []
        code = self.encoded_data
        for i in range(length):
            symbol_range = high - low
            scaled_code = (code - low) / symbol_range
            symbol = None
            for s, freq in self.cumulative_freqs.items():
                if scaled_code < (freq + 1) / len(code):
                    symbol = s
                    break
            if symbol is None:
                raise ValueError("Invalid encoded data")
            data.append(symbol)
            symbol_low = low + symbol_range * self.cumulative_freqs[symbol] / len(code)
            symbol_high = low + symbol_range * (self.cumulative_freqs[symbol] + 1) / len(code)
            low = symbol_low
            high = symbol_high
        return data
