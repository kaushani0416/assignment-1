# Define the DNA string
s = input("Enter the DNA sequence")

# Create a translation table 
translation_table = str.maketrans("ATCG", "TAGC")

# Reverse the string and apply the translation
s_c = s[::-1]

# apply the traslation to s_c
reverse_complement = s_c.translate(translation_table)

# Print the reverse complement
print(reverse_complement)
