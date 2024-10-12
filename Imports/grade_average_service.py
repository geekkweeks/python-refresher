def calculate_homework_assignment(homework_assignment_args):
    sum_of_grades = 0
    for homework in homework_assignment_args.values():
        sum_of_grades += homework
    print("🚀 ~ sum_of_grades:", sum_of_grades)
    final_grade = round(sum_of_grades / 
                        len(homework_assignment_args))
    print(final_grade)