def create_matrix(numbers, rows, columns):
    matrix = []
    count = 0
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(numbers[count])
            count += 1
        matrix.append(row)
    return matrix

numbers = set()
while len(numbers) < 9:
    num = int(input("Ingrese un número (no repetido): "))
    if num not in numbers:
        numbers.add(num)

numbers = list(numbers)
matrix = create_matrix(numbers, 3, 3)
print("Matriz:")
for row in matrix:
    print(row)
