def solution(answers):
    # Patterns for each student
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]  # Scores for each student
    
    # Iterate through answers and compare with each student's pattern
    for i, answer in enumerate(answers):
        if answer == student1[i % len(student1)]:
            scores[0] += 1
        if answer == student2[i % len(student2)]:
            scores[1] += 1
        if answer == student3[i % len(student3)]:
            scores[2] += 1
    
    # Find the maximum score
    max_score = max(scores)
    
    # Get the students who have the maximum score
    result = []
    for index, score in enumerate(scores):
        if score == max_score:
            result.append(index + 1)
    
    return result  # Return the list of top-scoring students

# Example usage
print(solution([1,2,3,4,5]))  # Output: [1]
print(solution([1,3,2,4,2]))  # Output: [1,2,3]