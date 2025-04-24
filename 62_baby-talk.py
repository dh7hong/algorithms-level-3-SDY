def solution(babbling):
    sounds = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        original_word = word  # Keep original for debugging (optional)
        
        # Replace each sound with a distinct digit to identify repetitions easily
        for idx, sound in enumerate(sounds):
            word = word.replace(sound, str(idx+1))
        
        # Check if the word has consecutive repeated digits (invalid)
        invalid = False
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                invalid = True
                break
        
        # If no invalid repetition and all letters replaced, it's pronounceable
        if not invalid and word.isdigit():
            count += 1

    return count

# Provided test cases:
print(solution(["aya", "yee", "u", "maa"]))  # Output: 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))  # Output: 2