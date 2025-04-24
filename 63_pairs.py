def solution(X, Y):
    # Initialize arrays to count digit occurrences (0 to 9)
    count_X = [0] * 10
    count_Y = [0] * 10

    # Count occurrences of each digit in X
    for digit in X:
        count_X[int(digit)] += 1

    # Count occurrences of each digit in Y
    for digit in Y:
        count_Y[int(digit)] += 1

    # Construct the largest number by pairing common digits
    result = ''
    for digit in range(9, -1, -1):  # Start from digit 9 down to 0
        common = min(count_X[digit], count_Y[digit])
        result += str(digit) * common  # Append the digit 'common' times

    # Handle special cases explicitly
    if result == '':
        return "-1"  # No common digit found
    elif result[0] == '0':
        return "0"   # All digits are zero
    else:
        return result  # Return the largest number constructed

# Test provided cases
print(solution("100", "2345"))    # Output: "-1"
print(solution("100", "203045"))  # Output: "0"
print(solution("100", "123450"))  # Output: "10"
print(solution("12321", "42531")) # Output: "321"
print(solution("5525", "1255"))   # Output: "552"
