/*Write a Python script that performs the following tasks:

1. Create Data:

Create a list of strings: ["apple", "banana", "cherry"].

2. Save Data:

Write a function named save_to_file(data, filename) that takes a list of strings and a filename as input and writes each string to a new line in a text file with the given filename.

3. Main Script:

Use the save_to_file(data, "fruits.txt") function to save the list of strings to a text file named "fruits.txt".
Ensure that the script creates the file and writes the strings correctly.
*/


#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    // List of strings
    vector<string> data = {"apple", "banana", "cherry"};

    // Open the file to write
    ofstream file("fruits.txt");

    // Write each item to the file
    for (const string& item : data) {
        file << item << endl;
    }

    file.close();
    cout << "Data has been saved to fruits.txt." << endl;

    return 0;
}

void Q7(){

  main();
}
