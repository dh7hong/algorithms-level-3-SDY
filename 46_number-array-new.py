def solution(s):
    # Dictionary to map English number words to their corresponding digits
    num_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", 
                "four": "4", "five": "5", "six": "6", "seven": "7", 
                "eight": "8", "nine": "9"}
    
    # Initialize an empty string to build the result
    result = ""
    i = 0  # Pointer to traverse the string
    
    # Traverse the string
    while i < len(s):
        # Try to match the longest possible word starting from index i
        for word in num_dict:
            print(f'word: {word}, s[i:i+len(word)]: {s[i:i+len(word)]}')
            if s[i:i+len(word)] == word:
                result += num_dict[word]  
                # Append the corresponding digit
                i += len(word)  
                print(f'Match found, appending: {num_dict[word]}, i: {i}')
                # Move the pointer ahead by the 
                # length of the matched word
                break
        else:
            # If no word matched, just append the current character
            print(f'No match, appending: {s[i]}, i: {i}')
            result += s[i]
            i += 1
    
    return int(result)  
    # Convert the final string to an integer and return
    
print(solution("one4seveneight"))
# Expected output: 1478
print(solution("23four5six7"))
# Expected output: 234567
print(solution("2three45sixseven"))
# Expected output: 234567
print(solution("123"))
# Expected output: 123
