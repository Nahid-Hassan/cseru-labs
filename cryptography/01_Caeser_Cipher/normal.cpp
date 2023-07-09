#include <bits/stdc++.h>
using namespace std;

string encrypt(string message, int shift) {
    string encrypt_message = "";

    for (char &ch : message) {
        if (isupper(ch)) {
            encrypt_message += char(int(ch + shift - 65) % 26 + 65); // A = 65
        } else if (islower(ch)) {
            encrypt_message += char(int(ch + shift - 97) % 26 + 97); // a = 97
        } else {
            encrypt_message += ch;
        }
    }

    return encrypt_message;
}

string decrypt(string message, int shift) {
    string decrypt_message = "";

    for (char &ch : message) {
        if (isupper(ch)) {
            decrypt_message += char(int(ch - shift - 65 + 26) % 26 + 65);
        } else if (islower(ch)) {
            decrypt_message += char(int(ch - shift - 97 + 26) % 26 + 97);
        } else {
            decrypt_message += ch;
        }
    }

    return decrypt_message;
}

int main() {
    string message;
    int shift;

    cout << "Enter the message: ";
    getline(cin, message);

    cout << "Enter the shift value: ";
    cin >> shift;

    string encrypted_message = encrypt(message, shift);
    cout << encrypted_message << endl;

    string decrypt_message = decrypt(encrypted_message, shift);
    cout << decrypt_message << endl;
}