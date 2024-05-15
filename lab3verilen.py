import random

def printList(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end='    ')
        print()

def sum_even_row_elements(A):
    total_sum = 0
    for i in range(len(A)):
        if i % 2 == 1:  # Cüt sətrlər üçün
            total_sum += sum(A[i])
    return total_sum

n = 4
m = 4
A = []

for i in range(n):
    A.append([])
    for j in range(m):
        A[i].append(random.randint(2, 6))

print("Əvəz olunmuş massiv:")
printList(A)
print()

even_row_sum = sum_even_row_elements(A)
print("Cüt sətrlərdəki elementlərin cəmi:", even_row_sum)
