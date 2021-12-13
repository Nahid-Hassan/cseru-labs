# include <bits/stdc++.h>
using namespace std;

int is_char(char ch) {
    if (ch >= 'A' && ch <= 'Z') return 1;
    if (ch >= 'a' && ch <= 'z') return 1;
    return 0;
}

int is_digit(char ch) {
    if (ch >= '0' && ch <= '9') return 1;
    return 0;
}

int is_vowel(char ch) {
    if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
        return 1;
    }
    return 0;
}


// 1-a
void count(string str) {
    int word_count = 1;
    int letter_count = 0;
    int digit_count = 0;
    int other_count = 0;

    for (int i = 0; i < str.size(); i++) {
        if (str[i] == ' ' && (is_char(str[i+1]) || is_digit(str[i+1]))) word_count++;
        if (is_char(str[i])) letter_count++;
        if (is_digit(str[i])) digit_count++;
        if (!is_digit(str[i]) && !is_char(str[i])) other_count++;
    }
  
    cout << "Number of words is = " << word_count << endl;
    cout << "Number of letter is = " << letter_count << endl;
    cout << "Number of digit is = " << digit_count << endl;
    cout << "Number of other words is = " << other_count << endl;
}

//1-b
void separate(string str) {
    char sep_letter[100], sep_digit[100], sep_other[100];
    int mark_letter = 0, mark_digit = 0, mark_other = 0;

    for (int i = 0; i < str.size(); i++) {
        if (is_char(str[i])) {
            sep_letter[mark_letter++] = str[i];
        }
        if (is_digit(str[i])) {
            sep_digit[mark_digit++] = str[i];
        }
        if (!is_char(str[i]) && !is_digit(str[i])) {
            sep_other[mark_other++] = str[i];
        }
    }

    cout << "All Characters: " << sep_letter << endl;
    cout << "All digit: " << sep_digit << endl;
    cout << "All other characters: " << sep_other << endl;
}

//1-c
void count_vowel_and_consonant(string str) {
    int vowel_count = 0; 
    int consonant_count = 0;

    for (int i = 0; i < str.size(); i++) {
        if (is_vowel(str[i])) {
            vowel_count++;
        } 
        if (is_char(str[i]) && !is_vowel(str[i])) {
            consonant_count++;
        }
    }

    cout << "Number of vowels: " << vowel_count << endl;
    cout << "Number of consonants: " << consonant_count << endl;
}


// 1-d
void vowel_and_consonant(string str) {
    char vowels[100], consonants[100];
    int mark_vowel=0, mark_consonanat=0;

    for (int i = 0; i < str.size(); i++) {
        if (is_vowel(str[i])) {
            vowels[mark_vowel++] = str[i];
        } 
        if (is_char(str[i]) && !is_vowel(str[i])) {
            consonants[mark_consonanat++] = str[i];
        }
    }


    cout << "Vowels are in the putting string is: " << vowels << endl;
    cout << "Consonants are in the putting string is: " << consonants << endl;
}

// 1-e
// divide the string into two separate string 
void word_start_with_vowel(string str) {
    
    for (int = 0; i < str.size(); i++) {
        
    }
}

int main() {
    string str = "Md. Tareq Zaman, Part-3,2011";
    cout << str << endl;

    count(str);
    separate(str);
    count_vowel_and_consonant(str);
    vowel_and_consonant(str);

    return 0;
}