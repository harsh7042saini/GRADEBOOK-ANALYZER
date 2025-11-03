def calculate_average(marks_dict):
    total = sum(marks_dict.values())
    count = len(marks_dict)
    average = total / count
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    marks = sorted(marks_dict.values())
    n=len(marks)
    mid = n // 2

    if n % 2 == 0:
        median = (marks[mid - 1] + marks[mid]) / 2
    else:
        median = marks[mid]
    return median

def find_max(marks_dict):
    return max(marks_dict.values())

def find_min(marks_dict):
    return min(marks_dict.values())

def grade_distribution(d):
    grades={"A":0,"B":0,"C":0,"D":0,"F":0}
    for i in d:
        if d[i]>=90:
            grades['A']+=1
        elif d[i]>=80:
            grades['B']+=1
        elif d[i]>=70:
            grades['C']+=1
        elif d[i]>=60:
            grades['D']+=1
        elif d[i]<50:
            grades['F']+=1
    return grades


def grading(d):
    grades={}
    for name, marks in d.items():
        if marks>=90:
            grades[name]='A'
        elif marks>=80:
            grades[name]='B'
        elif marks>=70:
            grades[name]='C'
        elif marks>=60:
            grades[name]='D'
        else:
            grades[name]='F'
    return grades

def manual_input():
    marks={}
    n = int(input("Enter no of student"))
    for i in range(n):
        name=input("Enter name of student")
        mark = int(input("Enter marks for(name)"))
        marks[name]=mark
        return marks
    

def display_results(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("-" * 30)
    for name in marks:
        print(f"{name}\t\t{marks[name]}\t{grade[name]}")

print("=== GradeBook Analyzer ===")

marks = manual_input()


avg = calculate_average(marks)
median = calculate_median(marks)
max_score = find_max(marks)
min_score = find_min(marks)

print("\n--- Statistical Summary ---")
print(f"Average Marks: {avg:.2f}")
print(f"Median Marks: {median}")
print(f"Highest Marks: {max_score}")
print(f"Lowest Marks: {min_score}")

grades = grading(marks)
distribution = grade_distribution(grades)

print("\n--- Grade Distribution ---")
for grade, count in distribution.items():
    print(f"{grade}: {count}")

passed_students = [name for name, mark in marks.items() if mark >=40]
failed_students  = [name for name, mark in marks.items() if mark < 40]

print(f"\nPassed Students ({len(passed_students)}): {passed_students}")
print(f"Failed Students ({len(failed_students)}): {failed_students}")
