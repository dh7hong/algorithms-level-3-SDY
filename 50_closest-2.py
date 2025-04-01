def find_previous_occurrence(index, s):
    # Loop B
    for j in range(index - 1, -1, -1):
        if s[index] == s[j]:
            return index - j
    return -1

def solution(s):
    result = []
    # Loop A
    for i in range(len(s)):
    
        result.append(find_previous_occurrence(i, s))
    
    return result
