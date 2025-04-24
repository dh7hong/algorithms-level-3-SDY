def solution(n, lost, reserve):
    # Convert lists to sets for efficient lookup and removal
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    # Handle intersection (students who appear in both lost and reserve)
    intersection = lost_set & reserve_set
    lost_set -= intersection
    reserve_set -= intersection
    
    # Try to lend gym clothes to lost students
    for student in sorted(lost_set):
        if student - 1 in reserve_set:  # Check the previous student
            reserve_set.remove(student - 1)
            lost_set.remove(student)
        elif student + 1 in reserve_set:  # Check the next student
            reserve_set.remove(student + 1)
            lost_set.remove(student)
    
    # Calculate and return the maximum number of students able to attend
    return n - len(lost_set)

# Provided test cases
print(solution(5, [2, 4], [1, 3, 5]))  # Output: 5
print(solution(5, [2, 4], [3]))        # Output: 4
print(solution(3, [3], [1]))           # Output: 2