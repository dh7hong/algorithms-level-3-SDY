def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    """Count the number of cases where the sum of three numbers is prime."""
    count = 0
    n = len(nums)
    
    # Generate all possible combinations of three numbers using nested loops
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if is_prime(nums[i] + nums[j] + nums[k]):
                    count += 1
    
    return count
