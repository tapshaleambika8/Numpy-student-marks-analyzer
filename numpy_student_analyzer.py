import numpy as np

# Student names
students = np.array([
    "Ambika", "Rahul", "Priya", "Amit", "Neha"
])

# Marks: rows = students, columns = subjects
marks = np.array([
    [85, 90, 88],
    [72, 75, 70],
    [95, 92, 96],
    [40, 55, 48],
    [78, 82, 80]
])

subjects = np.array(["Maths", "Python", "Computer Science"])

# 1. Calculate the class average
class_average = np.mean(marks)
print("Class Average:", round(class_average, 2))

# 2. Find the subject with the highest average
subject_averages = np.mean(marks, axis=0)
best_subject_index = np.argmax(subject_averages)

print("Subject Averages:", subject_averages)
print("Highest Average Subject:", subjects[best_subject_index])

# 3. Find students whose average is below 50
student_averages = np.mean(marks, axis=1)
low_performers = student_averages < 50

print("\nStudents with average below 50:")
print(students[low_performers])

# 4. Add a new student using np.vstack()
new_student_marks = np.array([[88, 91, 86]])

marks = np.vstack((marks, new_student_marks))
students = np.append(students, "Karan")

print("\nUpdated Student Names:")
print(students)

print("\nUpdated Marks:")
print(marks)

# 5. Save the final marks array using np.save()
np.save("student_marks.npy", marks)

print("\nMarks saved successfully to student_marks.npy")

# Bonus: Save student names and subject names too
np.save("student_names.npy", students)
np.save("subjects.npy", subjects)

print("Student names and subjects saved successfully!")