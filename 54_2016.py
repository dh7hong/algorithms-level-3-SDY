def solution(a, b):
    """
    This function returns the day of the week for the given month 
    (a) and day (b) in the year 2016.
    :param a: Month (1 to 12)
    :param b: Day (1 to 31, depending on the month)
    :return: The day of the week as a string 
    ("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT")
    """
    # List of days corresponding to indices (starting from Sunday)
    days_of_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    # Days in each month of 2016 (leap year)
    days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Calculate total days passed from January 1st to the given date
    total_days = sum(days_in_month[:a]) + b - 1  
    # Subtract 1 because Jan 1 is counted as the first day
    
    # Find the index of the day in days_of_week list
    return days_of_week[total_days % 7]

# Example usage:
print(solution(5, 24))  # Expected Output: "TUE"