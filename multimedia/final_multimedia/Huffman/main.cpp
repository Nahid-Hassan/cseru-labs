#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

struct Node {
    char data;
    int freq;
    Node* left;
    Node* right;
};

struct Compare {
    bool operator()(Node* left, Node* right) {
        return (left->freq > right->freq);
    }
};

unordered_map<char, string> huffman_encode_helper(Node* root) {
    unordered_map<char, string> huffman_code;
    if (!root) {
        return huffman_code;
    }
    if (!root->left && !root->right) {
        huffman_code[root->data] = "";
        return huffman_code;
    }
    unordered_map<char, string> left_code = huffman_encode_helper(root->left);
    for (auto& pair : left_code) {
        huffman_code[pair.first] = "0" + pair.second;
    }
    unordered_map<char, string> right_code = huffman_encode_helper(root->right);
    for (auto& pair : right_code) {
        huffman_code[pair.first] = "1" + pair.second;
    }
    return huffman_code;
}

unordered_map<char, string> huffman_encode(string data) {
    unordered_map<char, int> freq;
    for (char c : data) {
        freq[c]++;
    }
    priority_queue<Node*, vector<Node*>, Compare> pq;
    for (auto& pair : freq) {
        Node* node = new Node();
        node->data = pair.first;
        node->freq = pair.second;
        node->left = NULL;
        node->right = NULL;
        pq.push(node);
    }
    while (pq.size() != 1) {
        Node* left = pq.top();
        pq.pop();
        Node* right = pq.top();
        pq.pop();
        Node* parent = new Node();
        parent->data = '-';
        parent->freq = left->freq + right->freq;
        parent->left = left;
        parent->right = right;
        pq.push(parent);
    }
    Node* root = pq.top();
    unordered_map<char, string> huffman_code = huffman_encode_helper(root);
    delete root;
    return huffman_code;
}

string huffman_decode(string data, unordered_map<char, string>& codes) {
    string result = "";
    string code = "";
    for (char c : data) {
        code += c;
        for (auto& pair : codes) {
            if (pair.second == code) {
                result += pair.first;
                code = "";
            }
        }
    }
    return result;
}

int main() {
    string original_data = "hello world";
    unordered_map<char, string> codes = huffman_encode(original_data);
    string encoded_data = "";
    for (char c : original_data) {
        encoded_data += codes[c];
    }
    string decoded_data = huffman_decode(encoded_data, codes);
    cout << (original_data == decoded_data) << endl;  // prints 1 (true)
    return 0;
}
