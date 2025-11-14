
# DNA to protein (STAGE 1 TASK)

dna_blocks = ("AAATTGGCCAGCTTGATCTGATGC")
print(f"DNA sequence: {dna_blocks}")

# transcription: DNA to RNA
rna_blocks = dna_blocks.replace("T", "U")
print(f"RNA sequence: {rna_blocks}")

# codon table
protein_codons = {
    'AUA' :'I', 'AUC' :'I', 'AUU' :'I', 'AUG' :'M',
    'ACA' :'T', 'ACC' :'T', 'ACG' :'T', 'ACU' :'T',
    'AAC' :'N', 'AAU' :'N', 'AAA' :'K', 'AAG' :'K',
    'AGC' :'S', 'AGU' :'S', 'AGA' :'R', 'AGG' :'R',
    'CUA' :'L', 'CUC' :'L', 'CUG' :'L', 'CUU' :'L',
    'CCA' :'P', 'CCC' :'P', 'CCG' :'P', 'CCU' :'P',
    'CAC' :'H', 'CAU' :'H', 'CAA' :'Q', 'CAG' :'Q',
    'CGA' :'R', 'CGC' :'R', 'CGG' :'R', 'CGU' :'R',
    'GUA' :'V', 'GUC' :'V', 'GUG' :'V', 'GUU' :'V',
    'GCA' :'A', 'GCC' :'A', 'GCG' :'A', 'GCU' :'A',
    'GAC' :'D', 'GAU' :'D', 'GAA' :'E', 'GAG' :'E',
    'GGA' :'G', 'GGC' :'G', 'GGG' :'G', 'GGU' :'G',
    'UCA' :'S', 'UCC' :'S', 'UCG' :'S', 'UCU' :'S',
    'UUC' :'F', 'UUU' :'F', 'UUA' :'L', 'UUG' :'L',
    'UAC' :'Y', 'UAU' :'Y', 'UAA' :'Stop', 'UAG' :'Stop',
    'UGC' :'C', 'UGU' :'C', 'UGA' :'Stop', 'UGG' :'W',
}

# translation: RNA to protein
def codon_to_amino(rna_blocks, protein_codons):
    protein = ""
    for i in range (0, len(rna_blocks), 3):
        codon = rna_blocks[i:i + 3]

        amino_acid = protein_codons[codon]
        protein += amino_acid
        if protein.endswith("Stop"):
            protein = protein[:-4]
    return protein

protein = codon_to_amino(rna_blocks, protein_codons)

print(f"Protein sequence: {protein}")



# HAMMING DISTANCE

slack_username = "Oluwafoyinsola"
made_up_name = "Fioninuoluwa"

distance = sum(a != b for a ,b in zip(slack_username, made_up_name))
print (f"Slack username: {slack_username}")
print (f"Made up name: {made_up_name}")
print (f"Hamming Distance: {distance}")
