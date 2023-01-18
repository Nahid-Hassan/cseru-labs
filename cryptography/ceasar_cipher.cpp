#include <bits/stdc++.h>
using namespace std;

string encrypt_msg(string msg, int key) {
    string res = "";

    for (char s : msg) {
        if (isupper(s)) res += (char) (s + key - 65) % 26 + 65;
        else if (islower(s)) res += (char) (s + key - 97) % 26 + 97;
        else res += s;
    }

    return res;
}

string decrypt_msg(string msg, int key) {
    string res = "";
    
    for (char s : msg) {
        if (isupper(s)) res += (char) (s - key - 65 + 26) % 26 + 65;
        else if (islower(s)) res += (char) (s - key - 97 + 26) % 26 + 97;
        else res += s;
    }

    return res;
}

int main() {
    string msg;  
    // cout << "Enter your message: ";
    // cin >> msg;                     // original message
    msg = "xyzabc";

    int key;
    cout << "Enter your key: ";
    cin >> key;                     // key shift value 0-25

    string e_msg = encrypt_msg(msg, key);          // call encrypt function
    cout << e_msg << endl;

    string d_msg = decrypt_msg(e_msg, key);
    cout << d_msg << endl;

    return 0;
}

/**
XYZ
*/