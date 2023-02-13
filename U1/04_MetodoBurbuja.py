def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

numbers = []
num = int(input("¿Cuántos números desea ingresar? "))
for i in range(num):
    n = int(input("Ingrese un número: "))
    numbers.append(n)

print("Lista desordenada:", numbers)
bubble_sort(numbers)
print("Lista ordenada:", numbers)
