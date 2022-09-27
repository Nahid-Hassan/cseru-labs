#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    vector<vector<char>> in;
    vector<char> out;
    string s;


    while(getline(cin, s)) {
        bool flag = true;
        vector <char> temp;
        for (long unsigned int i = 1; i < s.size(); i++) {
            if (flag && isalpha(s[i])) {
                out.push_back(s[i]);
                flag = false;
                continue;
            }
            if (!flag && isalpha(s[i])) {
                temp.push_back(s[i]);
            }
        }
        in.push_back(temp);
    }
    
    for (long unsigned int i = 0; i < in.size(); i++) {
        for (long unsigned int j = i + 1; j < in.size(); j++) {
            if (find(in[i].begin(), in[i].end(), out[j]) != in[i].end()) {
                cout << "P" << i + 1 << " and P" << j + 1 << " are anti-independent.\n";
                continue;
            }
            if (find(in[j].begin(), in[j].end(), out[i]) != in[j].end()) {
                cout << "P" << i + 1 << " and P" << j + 1 << " are follow-dependent.\n";
                continue;
            }
            if (out[i] == out[j]) {
                cout << "P" << i + 1 << " and P" << j + 1 << " are output-dependent.\n";
                continue;
            }
            cout << "P" << i + 1 << " and P" << j + 1 << " are parallel.\n";
        }
    }
}