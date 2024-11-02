def insertion_sort_with_swap_count(arr):
    swap_count = 0
    n = len(arr)
    
    for i in range(1, n):
        k = i
        while k > 0 and arr[k] < arr[k - 1]:
            # Swap elements
            arr[k], arr[k - 1] = arr[k - 1], arr[k]
            swap_count += 1
            k -= 1
    
    return swap_count

#to input data
n = int(input("Enter the number of elements in the array (n): "))
arr = list(map(int, input(f"Enter {n} integers separated by spaces: ").split()))

# check if the input array has the correct number of elements
if len(arr) != n:
    print("Error: The number of elements provided does not match n.")
else:
    # Calculate and print the number of swaps
    swap_count = insertion_sort_with_swap_count(arr)
    print("Number of swaps performed:", swap_count)
