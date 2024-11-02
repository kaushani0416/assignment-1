def parse_fasta(data):
    fasta_dict = {}
    label = ""
    
    for line in data.splitlines():
        if line.startswith(">"):
            label = line[1:].strip()  
            fasta_dict[label] = "" 
        else:
            fasta_dict[label] += line.strip()  # Append DNA sequence to the label
    
    return fasta_dict

def gc_content(dna):
    gc_count = dna.count("G") + dna.count("C")
    return (gc_count / len(dna)) * 100

def highest_gc_content(fasta_dict):
    max_gc_id = ""
    max_gc_content = 0
    
    for label, dna in fasta_dict.items():
        gc = gc_content(dna)
        if gc > max_gc_content:
            max_gc_content = gc
            max_gc_id = label
    
    return max_gc_id, max_gc_content

# Read input until they enter an empty line
print("Enter the FASTA format data (press Enter on an empty line to finish):")
data_lines = []
while True:
    line = input()
    if line == "":
        break
    data_lines.append(line)
data = "\n".join(data_lines)

# data process
fasta_dict = parse_fasta(data)
result_id, result_gc_content = highest_gc_content(fasta_dict)

# Print the result
print(result_id)
print(f"{result_gc_content:.6f}")


