from src.assignment8.util import find_avg
n = 4
columns= ['NAME', 'ID', 'CLASS', 'MARKS']
data = [
            ['david', 1, 10, 95],
            ['mani', 2, 8, 82],
            ['selvam', 3, 11, 90],
            ['siva', 4, 9, 88]
        ]
print(find_avg(n, columns, data))
