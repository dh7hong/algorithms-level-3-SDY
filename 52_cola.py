def solution(a, b, n):
    total_colas = 0  
    # Variable to store the total number of colas received
    
    while n >= a:  
        # Continue the process while we have enough bottles to exchange
        new_colas = (n // a) * b  
        # Calculate the number of colas received in exchange
        total_colas += new_colas  
        # Add to the total count
        n = (n % a) + new_colas  
        # Update the number of bottles available for the next exchange
    
    return total_colas  # Return the total number of colas received

def solution2(a, b, n):
    # Base case: if not enough bottles to exchange, return 0
    if n < a:
        return 0

    # Number of new colas you can get this round
    new_colas = (n // a) * b
    # Remaining bottles after exchange
    remaining = (n % a) + new_colas

    # Return new_colas + what you can get in the next round
    return new_colas + solution2(a, b, remaining)
