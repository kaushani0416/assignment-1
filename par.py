def partition_array(A):
    # Get the pivot element, which is the first element in A
    pivot = A[0]
    # Arrays to store values <= pivot and > pivot
    left = []
    right = []
    
    # Loop through the rest of the array and partition accordingly
    for element in A[1:]:
        if element <= pivot:
            left.append(element)  # Elements <= pivot go to the left
        else:
            right.append(element)  # Elements > pivot go to the right
    
    # Combine the parts: elements <= pivot, pivot, elements > pivot
    return left + [pivot] + right


n = int(input("Enter the number of elements: "))
A = list(map(int, input("Enter the elements of the array: ").split()))

# to make sure the input is valid
if len(A) != n:
    print("Error: The number of elements does not match the given n.")
else:
    # Get the partitioned array
    B = partition_array(A)
    print("Partitioned array:", " ".join(map(str, B)))



