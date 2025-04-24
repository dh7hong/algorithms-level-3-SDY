def solution(s, n):
    result = ""  # Initialize the resulting encrypted string
    print(f'Input string: {s}, Shift: {n}')
    print(f"==============================")
    for char in s:  # Iterate through each character in the input string
        print(f'Current character: {char}')
        if char.isalpha():  # Check if the character is a letter (not a space)
            ascii_offset = ord('A') if char.isupper() else ord('a')
            print(f'ASCII offset: {ascii_offset}')  
            # Determine if it's uppercase or lowercase
            shifted = (ord(char) - ascii_offset + n) % 26 + ascii_offset
            print(f'(ord(char) - ascii_offset + n % 26) = {(ord(char) - ascii_offset + n % 26)}')
            print(f'Shifted by {n} Shifted ASCII: {shifted}')  
            # Shift the character within A-Z or a-z
            result += chr(shifted)  
            print(f'Result characters: {result}')
            print(f"==============================")
            # Convert ASCII back to a character and append it
        else:
            result += char  # If it's a space, keep it unchanged

    return result  # Return the final encrypted string

print(solution("zBC", 2))  # Expected output: "b c d"