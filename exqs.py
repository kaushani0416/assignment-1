def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swapping

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  
    return i + 1

def iterative_quick_sort(arr):
    # Initialize stack for indices
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            # Partition the array and get the pivot index
            pivot_index = partition(arr, low, high)
            # Push left and right subarrays to the stack
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

# Main program to take user input and display sorted array
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
            # Sort the array using iterative quick sort
            iterative_quick_sort(arr)
            # Output the sorted array
            print("Sorted array:", " ".join(map(str, arr)))
except ValueError:
    print("Invalid input. Please enter integers only.")
