#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    string filename = "data.txt";
    string textToWrite, textRead;
    
    // Writing to a file
    ofstream outFile(filename);
    if (!outFile) {
        cout << "Error creating file!" << endl;
        return 1;
    }
    
    cout << "Enter text to write to the file: ";
    getline(cin, textToWrite);
    
    outFile << textToWrite << endl;
    outFile.close();
    cout << "Data successfully written to " << filename << endl;
    
    // Reading from the file
    ifstream inFile(filename);
    if (!inFile) {
        cout << "Error opening file for reading!" << endl;
        return 1;
    }
    
    cout << "\n--- Reading from File ---" << endl;
    while (getline(inFile, textRead)) {
        cout << textRead << endl;
    }
    inFile.close();
    
    return 0;
}
