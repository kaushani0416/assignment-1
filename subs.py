def find_substring_positions(s, t):
    positions = []
    start = 0
    
    while True:
        # To locate substring
        pos = s.find(t, start)
        # Record positions
        if pos == -1:
            break
        # Positions are typically 1-indexed, so add 1 to pos
        positions.append(pos + 1)
        # Move start to the next position to look for further occurrences
        start = pos + 1
    
    return positions

s = input("Enter the main string (s): ")
t = input("Enter the substring to search for (t): ")


positions = find_substring_positions(s, t)
print("Positions:", " ".join(map(str, positions)))
