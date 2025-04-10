def solution(cards1, cards2, goal):
    # Initialize two pointers to track positions in cards1 and cards2
    index1, index2 = 0, 0
    
    # Iterate through each word in the goal list
    for word in goal:
        # Check if the word matches the current word in cards1
        if index1 < len(cards1) and cards1[index1] == word:
            index1 += 1  # Move to the next word in cards1
        # Check if the word matches the current word in cards2
        elif index2 < len(cards2) and cards2[index2] == word:
            index2 += 1  # Move to the next word in cards2
        else:
            # If the word does not match either, return "No"
            return "No"
    
    # If all words in goal are matched successfully, return "Yes"
    return "Yes"