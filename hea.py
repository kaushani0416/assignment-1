def max_heapify(arr, n, i):
    largest = i  # Initialize the largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    # Start from the last non-leaf node and go upwards
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

   # to take user input and display the max-heap
try:
    # Input the number of elements
    n = int(input("Enter the number of elements in the array (n): "))
    if n <= 0 or n > 10**5:
        print("Error: n should be a positive integer not exceeding 10^5.")
    else:
        # Input the array elements
        arr = list(map(int, input(f"Enter {n} integers separated by spaces: ").split()))
        if len(arr) != n:
            print("Error: Number of elements provided does not match n.")
        elif any(x < -10**5 or x > 10**5 for x in arr):
            print("Error: Array elements should be between -10^5 and 10^5.")
        else:
            # Build the max-heap
            build_max_heap(arr)
            # Output the heapified array
            print("Max-Heap array:", " ".join(map(str, arr)))
except ValueError:
    print("Invalid input. Please enter integers only.")
