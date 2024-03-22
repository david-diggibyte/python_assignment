def find_avg(n, columns, data):
    marks_index = columns.index('MARKS')
    total_marks = 0
    for row in data:
        total_marks += int(row[marks_index])
    average_marks = total_marks / n
    return float("{:.2f}".format(average_marks))

