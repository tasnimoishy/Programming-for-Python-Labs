students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]

def calculate_average(marks):
    return sum(marks) / len(marks)

def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"

def display_report(students):
    for s in students:
        average = calculate_average(s[2])
        performance = classify_performance(average)

        print("ID:", s[0])
        print("Name:", s[1])
        print("Average:", round(average, 2))
        print("Performance:", performance)
        print()

display_report(students)
