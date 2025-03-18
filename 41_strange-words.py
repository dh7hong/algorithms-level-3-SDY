def solution(s):
    answer = []
    words = s.split(" ")  
    # Split the string into words (preserving spaces)
    
    for word in words:
        formatted_word = []
        for idx, char in enumerate(word):
            print(f'idx: {idx}, char: {char}')
            if idx % 2 == 0:
                formatted_word.append(char.upper())
            else:
                formatted_word.append(char.lower())
        answer.append("".join(formatted_word))  
        # Join the formatted word and add to answer
    
    return " ".join(answer)  # Rejoin words with spaces

# Test case
print(solution("try hello world"))  
# Expected output: "TrY HeLlO WoRlD"

def solution2(s):
    return " ".join([
        "".join([
            char.upper() if idx % 2 == 0 else char.lower() 
            for idx, char in enumerate(word)
            ]) 
        for word in s.split(" ")
        ])
    
print(solution2("try hello world everyone"))

