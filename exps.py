def k_smallest_elements(n, A, k):
    # Sort the array A
    A.sort()
    return A[:k]


n = int(input("Enter the value of n: "))
A = list(map(int, input("Enter the elements of the array A: ").split()))
k = int(input("Enter the value of k: "))

# Get the k smallest elements
result = k_smallest_elements(n, A, k)


print("The k smallest elements are:", result)
