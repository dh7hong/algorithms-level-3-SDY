def solution2(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    # Calculate scores using list comprehension
    scores = [sum(a == pattern[i % len(pattern)] for i, a in enumerate(answers)) for pattern in patterns]

    max_score = max(scores)

    # Return students with the maximum score
    return [i + 1 for i, score in enumerate(scores) if score == max_score]

def solution(answers):
    # Patterns for each student
    patterns = [
        [1, 2, 3, 4, 5],                 # Student 1
        [2, 1, 2, 3, 2, 4, 2, 5],        # Student 2
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]   # Student 3
    ]

    scores = []

    # Calculate the score for each student
    for pattern in patterns:
        score = 0
        for i, answer in enumerate(answers):
            if answer == pattern[i % len(pattern)]:
                score += 1
        scores.append(score)

    # Find the maximum score among students
    max_score = max(scores)

    # Identify students who got the highest score
    top_students = []
    for i, score in enumerate(scores):
        if score == max_score:
            top_students.append(i + 1)  # Student numbers start from 1

    return top_students

# Example usage:
print(solution([1, 2, 3, 4, 5]))  # Output: [1]
print(solution([1, 3, 2, 4, 2]))  # Output: [1, 2, 3]
