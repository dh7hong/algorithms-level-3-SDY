def solution(food):
    arrangement = ""  # Initialize the arrangement string
    
    # Iterate over the food list, starting from index 1 (since index 0 is water)
    for i in range(1, len(food)):
        count = food[i] // 2  # Each player should get an equal amount
        arrangement += str(i) * count  # Append the food item count times
   
    # Create the right side of the arrangement by reversing the left side
    final_arrangement = arrangement + "0" + arrangement[::-1]
    
    return final_arrangement  # Return the final arrangement as a string

def solution2(food):
    arrangement = []  # Use a list to collect the left side of the arrangement

    # Iterate over the food list, starting from index 1 (index 0 is water)
    for i in range(1, len(food)):
        count = food[i] // 2  # Use only the even portion
        arrangement.extend([str(i)] * count)  # Extend 'i' count times

    # Build the full arrangement
    left = arrangement
    center = ["0"]
    right = arrangement[::-1]

    final_arrangement = left + center + right
    return ''.join(final_arrangement)  # Convert list to string before returning

def solution3(food):
    # Build the left half using list comprehension and join
    left = ''.join(str(i) * (food[i] // 2) for i in range(1, len(food)))
    
    # Build the full symmetric layout: left + water + reversed left
    return left + '0' + left[::-1]
