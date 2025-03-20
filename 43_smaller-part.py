def solution(t, p):
    count = 0
    p_length = len(p)
    t_length = len(t)
    for i in range(t_length - p_length + 1):
        if int(t[i:i + p_length]) <= int(p):
            count += 1
    return count
    
print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))