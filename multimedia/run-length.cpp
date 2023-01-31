#include <bits/stdc++.h>
using namespace std;

string encode(string text, int len) {
    string etext = "";
    for (int i = 0; i < len; i++) {
        int count = 1;
        while(i < len - 1 && text[i] == text[i+1]) {
            i++; count++;
        }
        etext += text[i];
        etext += to_string(count);
    }

    return etext;
}

string decode(string text, int len) {
    string dtext = "";
    for (int i = 0; i < len;) {
        if (isalpha(text[i])) {
            char ch = text[i];
            int num = 0;
            string nums = "";
            i++;

            while(text[i] >= '0' and text[i] <= '9') {
                nums += text[i];
                i++;
            }

            num = stoi(nums);

            for (int j = 0; j < num; j++) {
                dtext += ch;
            }
        }
    }

    return dtext;
}

int main() {
    string text = "wwwaaabbcxddddaxxxxxb";
    string etext = encode(text, text.size());
    cout << etext << endl;

    string dtext = decode(etext, etext.size());
    cout << dtext << endl;
}