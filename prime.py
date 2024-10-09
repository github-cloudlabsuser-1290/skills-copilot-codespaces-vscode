def prime(n): # Function to check if a number is prime
    if n == 1: # 1 is not prime
        return False
    for i in range(2, n): # Check for factors between 2 and n
        if n % i == 0: # n has a factor
            return False
    return True # n is prime