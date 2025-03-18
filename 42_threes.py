def solution(number):
    count = 0
    n = len(number)

    for i in range(n - 2):  # First student
        for j in range(i + 1, n - 1):  # Second student
            for k in range(j + 1, n):  # Third student
                if number[i] + number[j] + number[k] == 0:
                    count += 1

    return count

print(solution([-2, 3, 0, 2, -5]))  
# Expected output: 2
print(solution([-3, -2, -1, 0, 1, 2, 3]))  
# Expected output: 5
print(solution([-1, 1, -1, 1]))
# Expected output: 0