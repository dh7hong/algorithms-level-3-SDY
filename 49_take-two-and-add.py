def solution(numbers):
    # Create a set to store unique sums
    sum_set = set()
    
    # Get the length of the numbers list
    n = len(numbers)
    
    # Iterate through all possible pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            # Add the sum of the two numbers to the set
            sum_set.add(numbers[i] + numbers[j])
    
    # Convert the set to a sorted list and return it
    return sorted(sum_set)


def solution2(numbers):
    answer = []
    n_length = len(numbers)
    for i in range(n_length):
        print(f'i: {i}')
        for j in range(i + 1, n_length):
            print(f'i + 1: {i + 1}, j: {j}')
            print(f'numbers[i]: {numbers[i]}, numbers[j]: {numbers[j]}')    
            S = numbers[i] + numbers[j]
            print(f'numbers[i] + numbers[j] = {S}')
            answer.append(S)
            print(f'answer.append({S}): {answer}')
    
    answer = sorted(set(answer))
    
    return answer

print(solution2([2,1,3,4,1]))