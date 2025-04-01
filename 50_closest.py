def find_previous_occurrence(index, s):
    print(f'index: {index}, s: {s}')
    for j in range(index-1, -1, -1):
        # go through the string from the current index to the start
        print(f's: {s}, j: {j}, index: {index}')
        if s[index] == s[j]:
            # if the character at the current index is equal 
            # to the character at index j
            print(f's: {s}, j: {j}, index: {index}, index - j: {index - j}')
            return index - j
            # return the difference between the current index and index j
    return -1

def solution(s):

    result = []
    for index in range(len(s)):
        # for 'banana', the first index is 0, the second is 1, and so on until 5
        result.append(find_previous_occurrence(index, s))
        print(f'result: {result}')
    
    return result

print(solution("banana")) 