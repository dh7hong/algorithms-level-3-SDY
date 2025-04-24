def solution(lottos, win_nums):
    # Count the number of unreadable numbers (zeros)
    unreadable = lottos.count(0)
    
    # Count the number of correctly matched numbers (excluding zeros)
    matches = len(set(lottos) & set(win_nums))
    
    # Calculate highest possible matches and lowest possible matches
    highest_match = matches + unreadable
    lowest_match = matches
    
    # Function to convert match counts to prize tiers
    def get_prize_tier(match_count):
        if match_count >= 2:
            return 7 - match_count
        else:
            return 6  # no prize tier
    
    # Get the highest and lowest prize tiers
    highest_prize = get_prize_tier(highest_match)
    lowest_prize = get_prize_tier(lowest_match)
    
    return [highest_prize, lowest_prize]

# Provided test cases:
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1, 1]