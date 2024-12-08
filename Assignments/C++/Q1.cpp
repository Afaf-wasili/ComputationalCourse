/*

Q1:

Write a Python script that performs the following tasks:
The marks obtained by a student in 3 different subjects are input by the user. Your
program should calculate the average of subjects and display the grade. The student gets a
grade as per the following rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F
*/


#include <iostream>
using namespace std;

int main() {
    float subject1, subject2, subject3, average;
    char grade;

    cout << "Enter marks for three subjects: ";
    cin >> subject1 >> subject2 >> subject3;

    average = (subject1 + subject2 + subject3) / 3;

    if (average >= 90 && average <= 100) grade = 'A';
    else if (average >= 80) grade = 'B';
    else if (average >= 70) grade = 'C';
    else if (average >= 60) grade = 'D';
    else if (average >= 0) grade = 'F';
    else {
        cout << "Invalid marks entered.\n";
        return 1;
    }

    cout << "Average Marks: " << average << "\nGrade: " << grade << endl;
    return 0;
}
