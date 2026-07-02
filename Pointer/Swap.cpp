#include <iostream>
using namespace std;

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int num1, num2;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;
    
    cout << "Before Swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
    
    // Pass by reference using pointers
    swap(&num1, &num2);
    
    cout << "After Swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
    return 0;
}
