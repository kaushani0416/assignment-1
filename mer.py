def merge_sorted_arrays(A, B):
    # Combine and sort both arrays
    C = sorted(A + B)
    return C


n = int(input("Enter the number of elements in the first sorted array (n): "))
A = list(map(int, input(f"Enter {n} sorted integers for array A separated by spaces: ").split()))

m = int(input("Enter the number of elements in the second sorted array (m): "))
B = list(map(int, input(f"Enter {m} sorted integers for array B separated by spaces: ").split()))

# Ensure the input arrays have the correct number of elements
if len(A) != n or len(B) != m:
    print("Error: The number of elements provided does not match n or m.")
else:
    # Merge the arrays and print the result
    C = merge_sorted_arrays(A, B)
    print("Merged array C:", " ".join(map(str, C)))
