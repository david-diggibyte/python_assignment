def percentage(student_marks,name):
    len_students = len(student_marks[name])
    marks_total = sum(student_marks[name])
    avg = format(marks_total / len_students, '.2f')
    return avg

