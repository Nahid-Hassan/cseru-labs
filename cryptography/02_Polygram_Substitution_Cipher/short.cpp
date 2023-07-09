#include <bits/stdc++.h>
using namespace std;

unordered_map<string, string> encode, decode;

void generateDictionary() {
    ifstream input;
    input.open("dict.txt");

    string s1, s2;
    while (input >> s1 >> s2) {
        encode[s1] = s2;
        decode[s2] = s1;
    }

    input.close();
}

string process(string message, unordered_map<string, string>& dict) {
    string encrypt_message = "";
    string dummy = "";

    for (char c : message) {
        if (isalpha(c)) {
            dummy += c;

            if (dict.count(dummy)) {
                encrypt_message += dict.at(dummy);
                dummy = "";
            }
        } else {
            encrypt_message += c;
        }
    }

    return encrypt_message;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output_short.txt", "w", stdout);

    string message;

    cout << "Enter your message: ";
    getline(cin, message);
    cout << message << endl;

    generateDictionary();

    string encrypt_message = process(message, encode);
    cout << "Encrypted message: " << encrypt_message << endl;

    string decrypt_message = process(encrypt_message, decode);
    cout << "Encrypted message: " << decrypt_message << endl;

    return 0;
}