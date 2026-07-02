#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool isPalindrome(string str) {
    int left = 0;
    int right = str.length() - 1;
    
    while (left < right) {
        if (str[left] != str[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main() {
    string str;
    cout << "Enter a string: ";
    cin >> str;
    
    if (isPalindrome(str)) {
        cout << str << " is a Palindrome." << endl;
    } else {
        cout << str << " is NOT a Palindrome." << endl;
    }
    
    return 0;
}
