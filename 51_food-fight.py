def solution(food):
    arrangement = ""  # Initialize the arrangement string
    
    # Iterate over the food list, starting from index 1 (since index 0 is water)
    for i in range(1, len(food)):
        count = food[i] // 2  # Each player should get an equal amount
        arrangement += str(i) * count  # Append the food item count times
   
    # Create the right side of the arrangement by reversing the left side
    final_arrangement = arrangement + "0" + arrangement[::-1]
    
    return final_arrangement  # Return the final arrangement as a string