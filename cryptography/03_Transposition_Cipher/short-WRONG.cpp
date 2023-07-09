#include <bits/stdc++.h>
using namespace std;

string transposition(const string& message, const int key, bool isEncrypt) {
    int col = key;
    int row = ceil((double)message.size() / col);

    string result;
    result.reserve((int)message.size());

    for (int i = 0; i < col; i++) {
        for (int j = 0; j < row; j++) {
            int index = isEncrypt ? (j * col + i) : (i * row + j);
            if (index < (int)message.size()) {
                result += message[index];
            } else {
                result += ' ';
            }
        }
    }

    return result;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output_short.txt", "w", stdout);


    string message;
    int key;

    cout << "Enter the message: ";
    getline(cin, message);

    cout << "Enter the key: ";
    cin >> key;

    string encrypted_message = transposition(message, key, true);
    cout << "Encrypted message: " << encrypted_message << endl;

    string decrypted_message = transposition(encrypted_message, key, false);
    cout << "Decrypted message: " << decrypted_message << endl;

    return 0;
}
