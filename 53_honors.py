def solution(k, score):
    """
    This function calculates the lowest score in the Hall of Fame list each day.
    :param k: The number of scores in the Hall of Fame list
    :param scores: List of scores from each day
    :return: List of the lowest Hall of Fame scores each day
    """
    hall_of_fame = []  # List to store top k scores
    results = []  # List to store the lowest Hall of Fame scores each day
    
    for day, sc in enumerate(score):  # Iterate over each day's score
        hall_of_fame.append(sc)  # Add the current score to the list
        hall_of_fame.sort(reverse=True)  # Sort the list in descending order
        
        # If the Hall of Fame exceeds size k, remove the lowest ranked score
        if len(hall_of_fame) > k:
            hall_of_fame.pop()  # Remove the lowest ranked score
        
        # The lowest score in the Hall of Fame is always the last element
        results.append(hall_of_fame[-1])
    
    return results

# Example usage:
k = 3
scores = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, scores))  # Expected Output: [10, 10, 10, 20, 20, 100, 100]
