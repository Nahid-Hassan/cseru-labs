#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

class ArithmeticEncoder {
public:
    ArithmeticEncoder(vector<char>& symbols) : symbols_(symbols) {
        cumulative_freqs_ = calculate_cumulative_frequencies(symbols_);
    }
    
    double encode(vector<char>& data) {
        double low = 0;
        double high = 1;
        for (char symbol : data) {
            double symbol_range = high - low;
            double symbol_low = low + symbol_range * cumulative_freqs_[symbol] / data.size();
            double symbol_high = low + symbol_range * (cumulative_freqs_[symbol] + 1) / data.size();
            low = symbol_low;
            high = symbol_high;
        }
        return (low + high) / 2;
    }
    
private:
    vector<char> symbols_;
    unordered_map<char, int> cumulative_freqs_;
    
    unordered_map<char, int> calculate_cumulative_frequencies(vector<char>& symbols) {
        unordered_map<char, int> freqs;
        for (char symbol : symbols) {
            freqs[symbol]++;
        }
        unordered_map<char, int> cumulative_freqs;
        int current_sum = 0;
        for (const auto& p : freqs) {
            cumulative_freqs[p.first] = current_sum;
            current_sum += p.second;
        }
        return cumulative_freqs;
    }
};

class ArithmeticDecoder {
public:
    ArithmeticDecoder(vector<char>& symbols, double encoded_data) : symbols_(symbols) {
        cumulative_freqs_ = calculate_cumulative_frequencies(symbols_);
        encoded_data_ = encoded_data;
    }
    
    vector<char> decode(int length) {
        double low = 0;
        double high = 1;
        vector<char> data;
        for (int i = 0; i < length; i++) {
            double symbol_range = high - low;
            double scaled_code = (encoded_data_ - low) / symbol_range;
            char symbol = '\0';
            for (const auto& p : cumulative_freqs_) {
                if (scaled_code < (p.second + 1) / (double)length) {
                    symbol = p.first;
                    break;
                }
            }
            if (symbol == '\0') {
                throw "Invalid encoded data";
            }
            data.push_back(symbol);
            double symbol_low = low + symbol_range * cumulative_freqs_[symbol] / (double)length;
            double symbol_high = low + symbol_range * (cumulative_freqs_[symbol] + 1) / (double)length;
            low = symbol_low;
            high = symbol_high;
        }
        return data;
    }
    
private:
    vector<char> symbols_;
    unordered_map<char, int> cumulative_freqs_;
    double encoded_data_;
    
    unordered_map<char, int> calculate_cumulative_frequencies(vector<char>& symbols) {
        unordered_map<char, int> freqs;
        for (char symbol : symbols) {
            freqs[symbol]++;
        }
        unordered_map<char, int> cumulative_freqs;
        int current_sum = 0;
        for (const auto& p : freqs) {
            cumulative_freqs[p.first] = current_sum;
            current_sum += p.second;
        }
        return cumulative_freqs;
    }
};

int main() {
    vector<char> symbols = {'A', 'B', 'C', 'D'};
    vector<char> data = {'A', 'A', 'C', 'B', 'D'};
    
    // Encode the data
    ArithmeticEncoder encoder(symbols);
    double encoded_data = encoder.encode(data);
    
    // Decode the encoded data
    ArithmeticDecoder decoder(symbols, encoded_data);
    vector<char> decoded_data = decoder.decode(data.size());
    
    // Print the results
    cout << "Original data: ";
    for (char c : data) {
        cout << c << " ";
    }
    cout << endl;
    cout << "Encoded data: " << encoded_data << endl;
    cout << "Decoded data: ";
    for (char c : decoded_data) {
        cout << c << " ";
    }
    cout << endl;
    
    return 0;
}

/*
Original data: A A C B D 
Encoded data: 0.16125
Decoded data: A A C B D 
*/