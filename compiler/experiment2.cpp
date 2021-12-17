/*Build Lexical Analyzer implementing the following regular expressions.*/

#include <bits/stdc++.h>
using namespace std;

string str;

int is_valid(int start, int end) {
    for (int i = start; i <= end; i++) {
        if ((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= 'A' && str[i] <= 'Z') || (str[i] >= '0' && str[i] <= '9')) {
            continue;
        }
        return 0;
    }
    return 1;
}

bool is_all_digit() {
    for (auto ch : str) {
        if (ch >= '0' && ch <= '9') {
            continue;
        }
        return 0;
    }
    return 1;
}

int is_float() {
    int count = 0;
    int len = str.size();

    for (int i = 0; i < len; i++) {
        if (str[i] == '.') {
            for(int j = 0; j < len; j++) {
                if (i != j && (str[j] < '0' || str[j] > '9')) {
                    return 0;
                }
            }
        }
    }
}

int main(int argc, char const *argv[])
{


    return 0;
}
