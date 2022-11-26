#include <bits/stdc++.h>
using namespace std;

//!!WARNING: This code is not completed yet....!

int main() {
    freopen("in.txt", "r", stdin);
    int row, col, data;

    cin >> row >> col;
    vector <vector<int>> rt;
    
    for (int i = 0; i < row; i++) {
        vector <int> temp;
        for (int j = 0; j < col; j++) {
            cin >> data;
            temp.push_back(data);
        }
        rt.push_back(temp);
    }

    //!!TASK: forbidden latency
    set <int> st;
    for (int i = 0; i < rt.size(); i++) {
        for (int j = 0; j < rt[i].size(); j++) {
            if (rt[i][j]) {
                for (int k = j + 1; k < rt[i].size(); k++) {
                    if (rt[i][k]) {
                        st.insert(k - j);
                    }
                }
            }
        }
    }

    // set to vector
    vector <int> fl;
    for (auto it : st) fl.push_back(it); 

    cout << "Forbidden Latency Set: {";
    for (auto it : fl) cout << it << ", ";
    cout << "\b\b}\n";

    //!!TASK: permissible latency
     
    // create pl array with initial size equal col - forbidden_latency_size 
    vector <int> pl(col - fl.size(), 0);
    vector<int> universal;
    for (int i = 1; i <= col; i++) universal.push_back(i);

    set_difference(universal.begin(), universal.end(), fl.begin(), fl.end(), pl.begin());

    cout << "Permissible Latency Set: {";
    for (auto it : pl) cout << it << ", ";
    cout << "\b\b}\n";


    //!!TASK: collision vector
    vector <int> cv(fl[fl.size() - 1], 0); // upto max

    // change to zero for permissible latency
    for (int i = 0, j = 0; i < fl[fl.size() - 1]; i++) {
        if (i == fl[j] - 1) {
            cv[i] = 1;
            j++;
        }
    }
    reverse(cv.begin(), cv.end());
    cout << "Collision Vector: {";
    for (auto it : cv) cout << it << ", ";
    cout << "\b\b}\n";

}
