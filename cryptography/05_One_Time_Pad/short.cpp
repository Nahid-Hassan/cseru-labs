#include <bits/stdc++.h>
using namespace std;

string processText(string message, string pad, bool encrypt) {
    string result;
    for (int i = 0; i < (int)message.size(); i++) {
        if (isalpha(message[i])) {
            char base = isupper(message[i]) ? 'A' : 'a';
            int shift = encrypt ? 1 : -1;
            // 
            char encrypted_char = ((message[i] - base + shift * (pad[i] - base) + 26) % 26) + base;
            result += encrypted_char;
        } else {
            result += message[i];
        }
    }
    return result;
}

int main() {
    ifstream input("pad.txt");
    string pad;
    getline(input, pad);
    input.close();

    string message = "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING";
    string encrypt_message = processText(message, pad, true);
    string decrypt_message = processText(encrypt_message, pad, false);

    cout << "Encrypt message: " << encrypt_message << endl;
    cout << "Decrypt message: " << decrypt_message << endl;

    return 0;
}
