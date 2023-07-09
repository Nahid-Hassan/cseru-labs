#include <bits/stdc++.h>
using namespace std;

string encrypt(string message, int width) {
    int col = width;
    int row = ceil((double) message.size() / width);

    string encrypt_message = "";
    for (int j = 0; j < col; j++) {
        for (int i = 0; i < row; i++) {
            int index = i * width + j;

            if (index < (int) message.size()) {
                encrypt_message += message[index];
            } else {
                encrypt_message += " ";
            }
        }
    }

    return encrypt_message;
}

string decrypt(string message, int width) {
    int col = width;
    int row = ceil((double) message.size() / width);

    string decrypt_message = "";
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            int index = j * row + i;
            if (index < (int) message.size()) {
                decrypt_message += message[index];
            }
        }
    }
    return decrypt_message;
}
 
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output_normal.txt", "w", stdout);

    string message;
    int width;

    cout << "Enter your message: ";
    getline(cin, message);
    cout << message << endl;

    cout << "Enter the width: ";
    cin >> width;
    cout << width << endl;    

    string encrypt_message = encrypt(message, width);
    cout << "Encrypted message: " << encrypt_message << endl;

    string decrypt_message = decrypt(encrypt_message, width);
    cout << "Decrypted message: " << decrypt_message << endl;
}