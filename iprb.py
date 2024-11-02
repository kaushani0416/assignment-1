# genes AA dominant aa recessive

def dominant_phenotype_probability(k, m, n):
    # Total population
    total = k + m + n
    
    # Probabilities for all the possible outcomes
    P_AA_AA = (k / total) * ((k - 1) / (total - 1))
    P_AA_Aa = (k / total) * (m / (total - 1)) + (m / total) * (k / (total - 1))
    P_AA_aa = (k / total) * (n / (total - 1)) + (n / total) * (k / (total - 1))
    P_Aa_Aa = (m / total) * ((m - 1) / (total - 1))
    P_Aa_aa = (m / total) * (n / (total - 1)) + (n / total) * (m / (total - 1))

    # calculated probabilities for dominant phenotype
    probability = (
        P_AA_AA * 1.0 +
        P_AA_Aa * 1.0 +
        P_AA_aa * 1.0 +
        P_Aa_Aa * 0.75 +
        P_Aa_aa * 0.5
    )
    
    return probability

k = int(input("Enter the number of homozygous dominant (AA) organisms (k): "))
m = int(input("Enter the number of heterozygous (Aa) organisms (m): "))
n = int(input("Enter the number of homozygous recessive (aa) organisms (n): "))

# Print the result
print(dominant_phenotype_probability(k, m, n))