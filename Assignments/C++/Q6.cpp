/*Write a Python script that defines and uses the following functions:

1. is_even(n): A function that takes an integer n and returns True if the number is even, and False otherwise.

2. main(): A function that prompts the user to enter an integer and then:

A. Checks if the number is even using is_even(n) and prints "The number is even." if the function returns True.
B. If the function returns False, print "The number is odd."

Call the main() function to run the script.
*/


#include <iostream>
using namespace std;

int main() {
    int number;

    cout << "Enter an integer: ";
    cin >> number;

    // Checking if the number is even or odd
    if (number % 2 == 0) {
        cout << "The number is even." << endl;
    } else {
        cout << "The number is odd." << endl;
    }

    return 0;
}

