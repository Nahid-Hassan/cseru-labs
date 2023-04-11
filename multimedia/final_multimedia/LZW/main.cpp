#include <bits/stdc++.h>
using namespace std;

vector<int> lzw_encode(string data) {
    unordered_map<string, int> dictionary;
    vector<int> result;
    for (int i = 0; i < 256; i++) {
        string ch = "";
        ch += char(i);
        dictionary[ch] = i;
    }
    string w = "";
    for (char c : data) {
        string wc = w + c;
        if (dictionary.find(wc) != dictionary.end()) {
            w = wc;
        } else {
            result.push_back(dictionary[w]);
            dictionary[wc] = dictionary.size();
            w = string(1, c);
        }
    }
    if (!w.empty()) {
        result.push_back(dictionary[w]);
    }
    return result;
}

string lzw_decode(vector<int> data) {
    unordered_map<int, string> dictionary;
    string result = "";
    for (int i = 0; i < 256; i++) {
        string ch = "";
        ch += char(i);
        dictionary[i] = ch;
    }
    int w = data[0];
    result += dictionary[w];
    for (size_t i = 1; i < data.size(); i++) {
        size_t k = data[i];
        string entry;
        if (dictionary.find(k) != dictionary.end()) {
            entry = dictionary[k];
        } else if (k == dictionary.size()) {
            entry = dictionary[w] + dictionary[w][0];
        } else {
            throw "Bad compressed k";
        }
        result += entry;
        dictionary[dictionary.size()] = dictionary[w] + entry[0];
        w = k;
    }
    return result;
}

int main() {
    string original_data = "hello world";
    vector<int> encoded_data = lzw_encode(original_data);
    string decoded_data = lzw_decode(encoded_data);
    for (auto num : encoded_data) {
        cout << num << " ";
    }
    cout << endl;
    cout << decoded_data << endl;
    cout << (original_data == decoded_data) << endl;  // prints 1 (true)
    return 0;
}
