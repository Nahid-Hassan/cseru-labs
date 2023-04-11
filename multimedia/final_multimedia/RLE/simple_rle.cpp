#include <iostream>
#include <string>
using namespace std;

string rle_encode(string text) {
    string encoded_text = "";
    int count = 1;
    char prev_char = text[0];
    for (size_t i = 1; i < text.length(); i++) {
        if (text[i] == prev_char) {
            count++;
        }
        else {
            encoded_text += to_string(count) + prev_char;
            count = 1;
            prev_char = text[i];
        }
    }
    encoded_text += to_string(count) + prev_char;
    return encoded_text;
}

string rle_decode(string encoded_text) {
    string decoded_text = "";
    string count_str = "";
    for (char c : encoded_text) {
        if (isdigit(c)) {
            count_str += c;
        }
        else {
            int count = stoi(count_str);
            decoded_text += string(count, c);
            count_str = "";
        }
    }
    return decoded_text;
}

int main() {
    string text = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBCCCC";
    string encoded_text = rle_encode(text);
    cout << encoded_text << endl;  // outputs: "4A4B4C"
    string decoded_text = rle_decode(encoded_text);
    cout << decoded_text << endl;  // outputs: "AAAABBBBCCCC"
    return 0;
}
