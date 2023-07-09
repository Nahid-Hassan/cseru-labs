#include <bits/stdc++.h>
using namespace std;

string encrypt(string message, string pad) {
    string encrypt_message = "";

    for (int i = 0; i < (int) message.size(); i++) {
        if (isalpha(message[i])) {
            char base = isupper(message[i]) ? 'A' : 'a';
            // (message - base + pad - base) % 26 + base
            encrypt_message += ((message[i] - base + pad[i] - base) % 26) + base;
        } else {
            encrypt_message += message[i];
        }
    }

    return encrypt_message;
}

string decrypt(string message, string pad) {
    string decrypt_message = "";

    for (int i = 0; i < (int)message.size(); i++) {
        if (isalpha(message[i])) {
            char base = isupper(message[i]) ? 'A' : 'a';
            // (message - base - pad + base + 26) % 26 + base;
            decrypt_message += (message[i] - base - pad[i] + base + 26) % 26 + base;
        } else {
            decrypt_message += message[i];
        }
    }

    return decrypt_message;
}

int main() {
    freopen("pad.txt", "r", stdin);
    string pad;
    getline(cin, pad);

    string message = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING";

    string encrypt_message = encrypt(message, pad);
    cout << "Encrypt message: " << encrypt_message << endl;

    string decrypt_message = decrypt(encrypt_message, pad);
    cout << "Decrypt message: " << decrypt_message << endl;

    return 0;
}