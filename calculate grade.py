def calculate_grade(average_marks):
    if average_marks >= 90:
        return 'A'
    elif 80 >= average_marks < 90:
        return 'B'
    elif 70 >= average_marks < 80:
        return 'C'
    elif 60 >= average_marks < 70:
        return 'D'
    else:
        return 'F'

# Input: Number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Initialize total marks
total_marks = 0

# Input: Marks for each subject
for i in range(1, num_subjects + 1):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total_marks += marks

# Calculate average marks
average_marks = total_marks / num_subjects

# Print average marks
print(f"Average Marks: {average_marks}")

# Calculate and print the grade
grade = calculate_grade(average_marks)
print(f"Grade: {grade}")
