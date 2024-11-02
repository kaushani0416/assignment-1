def hamming_distance(s, t):
    
    # Initialize distance counter
    distance = 0
    
    # loop throught the indices of s and t,for each index i
    for i in range(len(s)):
        # If characters differ, increase the distance counter
        if s[i] != t[i]:
            distance += 1
    return distance
 
 
 # input data
s = input("Enter the first string (s): ")
t = input("Enter the second string (t): ")

# Calculate and print Hamming distance
try:
    distance = hamming_distance(s, t)
    print("Hamming Distance:", distance)
except ValueError as e:
    print(e)
