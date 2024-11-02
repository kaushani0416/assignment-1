def rabbit_pairs(n, k):
    # Initial conditions for the sequence
    #f1 and f2  to represent the rabbit pairs in the 1st/2nd months
    F1, F2 = 1, 1

    # If n is 1 or 2, the result is 1
    if n == 1 or n == 2:
        return 1

    # Calculate up to the n-th month
    for month in range(3, n + 1):
        Fn = F2 + k * F1
        F1, F2 = F2, Fn  # Update for next iteration

    return Fn

# Sample dataset
n = int(input("Enter the number of months: "))
k = int(input("Enter the number of rabbit pairs: "))
print(rabbit_pairs(n, k))
