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

string encrypt(string message) {
    string encrypt_message = "";
    string dummy = "";

    for (char c : message) {
        if (isalpha(c)) {
            dummy += c;

            if (encode.find(dummy) != encode.end()) {
                encrypt_message += encode[dummy];
                dummy = "";
            }
        } else {
            encrypt_message += c;
        }
    }

    return encrypt_message;
}

string decrypt(string message) {
    string decrypt_message = "";
    string dummy = "";

    for (char c : message) {
        if (isalpha(c)) {
            dummy += c;

            if (decode.find(dummy) != decode.end()) {
                decrypt_message += decode[dummy];
                dummy = "";
            }
        } else {
            decrypt_message += c;
        }
    }

    return decrypt_message;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output_normal.txt", "w", stdout);

    string message;

    cout << "Enter your message: ";
    getline(cin, message);
    cout << message << endl;

    generateDictionary();

    string encrypt_message = encrypt(message);
    cout << "Encrypted message: " << encrypt_message << endl;

    string decrypt_message = decrypt(encrypt_message);
    cout << "Encrypted message: " << decrypt_message << endl;

    return 0;
}