def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  
        left = [x for x in arr if x < pivot]  
        middle = [x for x in arr if x == pivot] 
        right = [x for x in arr if x > pivot]  
        return quick_sort(left) + middle + quick_sort(right) 



n = int(input("Enter the value of n: "))
A = list(map(int, input("Enter the elements of the array A: ").split()))

# Sort the array using quick sort
sorted_array = quick_sort(A)

# Print the sorted array
print("The sorted array is:", sorted_array)
