def partition_array(A):
    # Select the pivot as the first element in A
    pivot = A[0]
    
    # Arrays to store values < pivot, == pivot, and > pivot
    less = []
    equal = []
    greater = []
    
    # Partition the elements based on comparison with pivot
    for element in A:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
    
    # Combine the parts: elements < pivot, elements == pivot, elements > pivot
    return less + equal + greater


n = int(input("Enter the number of elements: "))
A = list(map(int, input("Enter the elements of the array: ").split()))

# Make sure the input is valid
if len(A) != n:
    print("Error: The number of elements does not match the given n.")
else:
    # Get the partitioned array
    B = partition_array(A)
    print("Partitioned array:", " ".join(map(str, B)))

