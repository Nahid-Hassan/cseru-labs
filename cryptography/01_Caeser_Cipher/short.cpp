#include <bits/stdc++.h>
using namespace std;

string encrypt(string message, int shift) {
    for (char& c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            c = ((c - base + shift) % 26) + base;
        }
    }

    return message;
}

string decrypt(string encrypted_message, int shift) {
    for (char& c : encrypted_message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            c = ((c - base - shift + 26) % 26) + base;
        }
    }

    return encrypted_message;
}

int main() {
    string message;
    int shift;

    cout << "Enter the message: ";
    getline(cin, message);

    cout << "Enter the shift value: ";
    cin >> shift;

    string encrypted_message = encrypt(message, shift);
    cout << "Encrypted message: " << encrypted_message << endl;

    string decrypted_message = decrypt(encrypted_message, shift);
    cout << "Decrypted message: " << decrypted_message << endl;

    return 0;
}
