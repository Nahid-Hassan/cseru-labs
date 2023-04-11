#include <bits/stdc++.h>
using namespace std;

void rle_encode(const string &input_file, const string &compressed_file) {
    ifstream fin(input_file);
    ofstream fout(compressed_file);

    string text;
    while(getline(fin, text)) {
        string encoded_text = "";
        int count = 1;
        char prev_char = text[0];

        for (size_t i = 1; i < text.length(); i++) {
            if (text[i] == prev_char) {
                count++;
            } else {
                fout << (to_string(count) + prev_char);
                count = 1;
                prev_char = text[i]; 
            }
        }
        fout << (to_string(count) + prev_char);
        fout << endl;
    }
}

void rle_decode(const string &compressed_file, const string &decompressed_file) {
    ifstream fin(compressed_file);
    ofstream fout(decompressed_file);
    string text;

    while (getline(fin, text)) {
        string decoded_text = "";
        string count_str = "";

        for (char c : text) {
            if (isdigit(c)) {
                count_str += c;
            } else {
                int count = stoi(count_str);
                decoded_text += string(count, c);
                count_str = "";
            }
        }
        fout << decoded_text;
        fout << endl;
    }
}

int main() {
    string input_file = "in.txt";
    string compressed_file = "compressed.txt";
    string decompressed_file = "decompressed.txt";

    rle_encode(input_file, compressed_file);
    rle_decode(compressed_file, decompressed_file);
}
