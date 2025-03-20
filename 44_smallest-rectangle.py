def solution(sizes):
    max_width = 0
    max_height = 0
    
    for width, height in sizes:
        print(f'original width: {width}, original height: {height}')
        width, height = max(width, height), min(width, height)
        print(f'new width: {width}, new height: {height}')
        max_width = max(max_width, width)
        print(f'new max_width: {max_width}')
        max_height = max(max_height, height)
        print(f'new max_height: {max_height}')
    return max_width * max_height

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
# Expected output: 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
# Expected output: 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
# Expected output: 133