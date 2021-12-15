/* Convert infix notation to postfix notation in cpp */
#include <bits/stdc++.h>
using namespace std;

int prec(char ch)
{
    switch (ch)
    {
    case '+':
    case '-':
        return 1;
    case '*':
    case '/':
        return 2;
    case '^':
        return 3;
    }
    return -1;
}

string infix_to_postfix(string str) {
    stack <char> st;
    string postfix = "";

    for (int i = 0; i < str.length(); i++) {
        if (str[i] >= 'a' && str[i] <= 'z' || str[i] >= 'A' && str[i] <= 'Z') {
            postfix += str[i];
        } else if (str[i] == '(') {
            st.push(str[i]);
        } else if (str[i] == ')') {
            while (!st.empty() && st.top() !=  '(') {
                postfix += st.top();
                st.pop();
            }
            if(!st.empty()) {
                st.pop();
            }
        } else {
            while(!st.empty() && prec(st.top()) > prec(str[i])) {
                postfix += st.top();
                st.pop();
            }
            st.push(str[i]);
        }
    }

    while(!st.empty()) {
        postfix += st.top();
        st.pop();
    }


    return postfix;
}

int main(int argc, char const *argv[])
{
    cout << "Enter the infix notation expression as string: ";
    string infix;
    cin >> infix;

    string postfix = infix_to_postfix(infix);
    cout << "Postfix notation for given infix notation is: " <<  postfix << endl;

    return 0;
}


/** Demonstration for input "(A-B)*(D/E)" 
 * 
 * i = 0: ( push on the stack. # (
 * i = 1: A 
 * i = 2: - push on the stack. # (-
 * i = 3: B
 * i = 4: ) # () is popped and * is popped stack is empty.
 * i = 5: ( push on the stack.
 * i = 6: D
 * i = 7: / push on the stack.
 * i = 8: E
 * i = 9: # () is popped and / is popped stack is empty.
 * 
 * "AB-DE/"
*/