def find_kth_smallest(arr, k):
    # Sort the array in ascending order
    arr.sort()
    # Return the k-th smallest element (1-indexed)
    return arr[k - 1]


n = int(input("Enter the number of elements in the array (n): "))
arr = list(map(int, input(f"Enter {n} integers separated by spaces: ").split()))
k = int(input(f"Enter the position of the smallest element to find (k, where 1 <= k <= {n}): "))

# Ensure the inputs are within the required range
if not (1 <= k <= n):
    print("Error: k must be between 1 and n.")
elif len(arr) != n:
    print("Error: The number of elements provided does not match n.")
else:
    # Find and print the k-th smallest element
    kth_smallest = find_kth_smallest(arr, k)
    print(f"The {k}-th smallest element is: {kth_smallest}")
