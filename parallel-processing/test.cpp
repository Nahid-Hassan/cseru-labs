#include <bits/stdc++.h>
using namespace std;

int main(int argc, char **argv) {
    freopen("in.txt", "r", stdin);
    // freopen("out.txt", "w", stdout);
    

    string s;
    vector<vector<char>> in;
    vector<char> out;

    while(getline(cin, s)) {
        bool flag = true;
        vector<char> temp;
        for (long unsigned int i = 1; i < s.size(); i++) {
            if (flag && isalpha(s[i])) {
                out.push_back(s[i]);
                flag = false;
            } else if (!flag && isalpha(s[i])) {
                temp.push_back(s[i]);
            }
        }
        in.push_back(temp);
    }

    // for (long unsigned int i = 0; i < out.size(); i++) {
    //     cout << out[i] << " ";
    // } cout << endl;

    // for (long unsigned int i = 0; i < in.size(); i++) {
    //     for (long unsigned int j = 0; j < in[i].size(); j++) {
    //         cout << in[i][j] << " ";
    //     } cout << endl;
    // }

    for (long unsigned int i = 0; i < out.size(); i++) {
        for (long unsigned int j = i + 1; j < out.size(); j++) {
            if (find(in[i].begin(), in[i].end(), out[j]) != in[i].end()) {
                cout << i + 1 << " " << j + 1 << " is not parallel\n";
                continue;
            }

            if (find(in[j].begin(), in[j].end(), out[i]) != in[j].end()) {
                cout << i + 1 << " " << j + 1 << " is not parallel\n";
                continue;
            }

            if (out[i] == out[j]) {
                cout << i + 1 << " " << j + 1 << " is not parallel\n";
                continue;
            }
            cout << i + 1 << " " << j + 1 << " are parallel\n";
        }
    }

    return 0;
}