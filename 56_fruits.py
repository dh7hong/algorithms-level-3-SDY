def solution(k, m, score):
    # Sort the scores in descending order to prioritize high scores first
    score.sort(reverse=True)
    # [3,3,2,2,1,1,1]
    max_profit = 0  # Variable to store the maximum profit
    
    # Process the scores in chunks of size m
    for i in range(0, len(score) - m + 1, m):
        # The minimum score in the current box (m-sized group) 
        # determines the price
        min_score_in_box = score[i + m - 1]
        
        # Calculate the profit for this box 
        # and add it to the total profit
        max_profit += min_score_in_box * m
    
    return max_profit  # Return the maximum profit obtained

# Example usage
k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]
print(solution(k, m, score))  # Output: 8