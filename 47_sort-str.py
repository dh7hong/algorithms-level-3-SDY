def solution(strings, n):
    """
    Sorts a list of strings based on the character at index 'n'. 
    If characters are the same, sorts lexicographically (dictionary order).
    
    Args:
        strings (list of str): List of strings to be sorted.
        n (int): Index of character used for sorting.
    
    Returns:
        list of str: Sorted list of strings.
    """

    # Outer loop: Iterate over each string in the list
    for i in range(len(strings)):
        # Inner loop: Compare current string with the remaining strings
        for j in range(i + 1, len(strings)):  
            
            # Condition 1: If the character at index 'n' in strings[i] 
            # is greater than in strings[j], swap them
            if strings[i][n] > strings[j][n]:
                strings[i], strings[j] = strings[j], strings[i]  
                # Swap to ensure correct order
            
            # Condition 2: If the characters at index 'n' are the same, 
            # sort lexicographically (alphabetically)
            # ["abce", "abcd"] -> ["abcd", "abce"]
            elif strings[i][n] == strings[j][n] and strings[i] > strings[j]:
                strings[i], strings[j] = strings[j], strings[i]  
                # Swap to ensure alphabetical order
    
    # Return the sorted list after applying both sorting conditions
    return strings

print(solution(["sun", "bed", "car"], 1))  # ['car', 'bed', 'sun']
print(solution(["abce", "abcd", "cdx"], 2))  # ['abcd', 'abce', 'cdx']