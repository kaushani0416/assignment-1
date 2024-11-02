# RNA codon table
codon_table = {
    'AUG': 'M', 'UGG': 'W', 'GUG': 'V', 'AUA': 'I', 'AUC': 'I', 'AUU': 'I',
    'AAG': 'K', 'AAA': 'K', 'AGG': 'R', 'AGA': 'R', 'ACG': 'T', 'ACC': 'T',
    'ACA': 'T', 'ACU': 'T', 'AAC': 'N', 'AAU': 'N', 'AGC': 'S', 'AGU': 'S',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGG': 'R', 'CGA': 'R',
    'CGC': 'R', 'CGU': 'R', 'CCG': 'P', 'CCC': 'P', 'CCA': 'P', 'CCU': 'P',
    'GAA': 'E', 'GAG': 'E', 'GAU': 'D', 'GAC': 'D', 'GGG': 'G', 'GGA': 'G',
    'GGC': 'G', 'GGU': 'G', 'GCG': 'A', 'GCC': 'A', 'GCA': 'A', 'GCU': 'A',
    'UAC': 'Y', 'UAU': 'Y', 'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCG': 'S', 'UCA': 'S', 'UCC': 'S', 'UCU': 'S', 'UGC': 'C', 'UGU': 'C',
    'UAA': '', 'UAG': '', 'UGA': ''  # Stop codons
}

def translate_rna_to_protein(rna):
    protein = []
    
    # Iterate over the RNA string in steps of 3 to get each codon
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        # Get the amino acid for the codon, stop if it is a stop codon
        amino_acid = codon_table.get(codon, '')
        if amino_acid == '':
            break
        protein.append(amino_acid)
    
    # Join the amino acids to form the protein string
    return ''.join(protein)

# Sample dataset
rna_string = input("enter the RNA sequence:")
protein_sequence = translate_rna_to_protein(rna_string)
print(f"Protein sequence: {protein_sequence}")

