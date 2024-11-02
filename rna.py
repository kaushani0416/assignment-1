# Given DNA string
t = input("Enter the DNA sequence")

# Initialize an empty RNA string
u = ""

# Loop through each character in the DNA string
for nucleotide in t:
    if nucleotide == "T":
        u += "U"  # Replace 'T' with 'U'
    else:
        u += nucleotide  # Keep other characters as is

# Output the RNA string
print(u)