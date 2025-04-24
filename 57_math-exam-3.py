def solution(answers):
    # Patterns for each student
    patterns = [
        [1, 2, 3, 4, 5],                # Student 1
        [2, 1, 2, 3, 2, 4, 2, 5],       # Student 2
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # Student 3
    ]

    scores = [0, 0, 0]  # Initialize scores for each student

    # Calculate the score for each student without using enumerate
    for i in range(len(answers)):
        # Student 1
        if answers[i] == patterns[0][i % len(patterns[0])]:
            scores[0] += 1
        # Student 2
        if answers[i] == patterns[1][i % len(patterns[1])]:
            scores[1] += 1
        # Student 3
        if answers[i] == patterns[2][i % len(patterns[2])]:
            scores[2] += 1

    # Find the maximum score
    max_score = max(scores)

    # Collect the students who have the highest score
    top_students = []
    for i in range(len(scores)):
        if scores[i] == max_score:
            top_students.append(i + 1)  # Student numbering starts at 1

    return top_students

# Example usage:
print(solution([1, 2, 3, 4, 5]))  # Output: [1]
print(solution([1, 3, 2, 4, 2]))  # Output: [1, 2, 3]
