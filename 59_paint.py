def solution(n, m, section):
    count = 0          # initialize roller stroke count
    painted = 0        # represents the right-most position painted so far

    for sec in section:
        # if the current section is already painted, skip it
        if sec <= painted:
            continue

        # if the current section is unpainted, use the roller here
        painted = sec + m - 1  # paint from sec to (sec + m - 1)
        count += 1             # increase the roller stroke count

    return count

# Testing examples provided:
print(solution(8, 4, [2, 3, 6]))  # Output: 2
print(solution(5, 4, [1, 3]))     # Output: 1
print(solution(4, 1, [1, 2, 3, 4])) # Output: 4
