def solution(s):
    # Dictionary to map English number words to their corresponding digits
    num_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
                "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    
    # Iterate through the dictionary and replace 
    # occurrences of number words with their digits
    for word, digit in num_dict.items():
        print(f'word: {word}, digit: {digit}, s: {s}')
        s = s.replace(word, digit)  
        print(f'after replace: {s}')
        # Replace all occurrences of the word with its corresponding digit
    
    return int(s)  # Convert the final string to an integer and return

print(solution("one4seveneight"))
# Expected output: 1478
print(solution("23four5six7"))
# Expected output: 234567
print(solution("2three45sixseven"))
# Expected output: 234567
print(solution("123"))
# Expected output: 123