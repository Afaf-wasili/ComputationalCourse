# Input marks for three subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Calculate the average
average = (subject1 + subject2 + subject3) / 3

# Determine the grade based on the average
if 90 <= average <= 100:
    grade = 'A'
elif 80 <= average < 90:
    grade = 'B'
elif 70 <= average < 80:
    grade = 'C'
elif 60 <= average < 70:
    grade = 'D'
elif 0 <= average < 60:
    grade = 'F'
else:
    grade = 'Invalid marks'

# Display the average and grade
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
