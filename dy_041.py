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
