# Grading Student Based on Marks Obtained by Making Functions
# Suppose you just attended a University examination. 
# The marks you obtained in various subjects are stored in a list like this:

# You want to find the average marks you obtained in the exam.

# Based on the average marks you want to find your grade as:
# You will get Grade A if the average marks is equal to or above 80 (A >= 80)
# You will get Grade B if the average marks is equal to or above 60 and less than 80 (B >= 60 and B < 80)
# You will get Grade C if the average marks is equal to or above 50 and less than 60 (C >= 50 and < 60)
# And if the average marks is less than 50, you will get Grade F (F < 50)

def calculate_average(marks):
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)
    return average_marks

def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60 and average_marks < 80:
        grade = 'B'
    elif average_marks >= 50  and average_marks < 60:
        grade = 'C'
    else:
        grade = 'F'
    return grade


marks = [40, 60, 50, 70, 55] 
average_marks = calculate_average(marks)
grade_result = compute_grade(average_marks)
print(f'The average mark for the student is {average_marks}')
print(f' The grade obtained by the student is {grade_result}')
