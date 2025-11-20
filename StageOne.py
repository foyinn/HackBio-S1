import sys

#DNA to protein
# DNA to uppercase
def clean_strand():
    c_strand = dna_blocks.upper()
    return c_strand

dna_blocks = "AGCcCTCAaAATCTatcGCCATTGTGTTTACAGATAATTTCCGGGCTCGTTC"
clean_strand = clean_strand()

print(f"DNA sequence: {dna_blocks}")

print(f"Template DNA Strand: {clean_strand}")

# Transcribe coding strand to RNA
RNA_block = str.maketrans({"A":"U",
                           "G":"C",
                           "C":"G",
                           "T":"A"})
def m_rna():
    rna = clean_strand.translate(RNA_block)
    return rna

m_rna = m_rna()
print(f"RNA Strand: {m_rna}")



# codon table
codons = {
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

def codon_to_amino(m_rna, codons):
    protein = ""
    for i in range (0, len(m_rna), 3):
        codon = m_rna[i:i+3]
        protein += codons[codon]
        if codons[codon] != "Stop":
            print(f"{codon}: {protein}")
        elif len(codon) < 3:
            break
        elif codons[codon] == "Stop":
            break

    return protein
protein = codon_to_amino(m_rna, codons)

print(f"Protein: {protein}")




# HAMMING DISTANCE

# function to calculate hamming distance
def cal_hamming_distance():
    distance = sum(a != b for a, b in zip(slack_username, made_up_name))
    return distance

slack_username = "Oluwaflowoyinsola"
made_up_name = "Fioninuoluwa"
distance = cal_hamming_distance()


print (f"Slack username: {slack_username}")
print (f"Made up name: {made_up_name}")
print (f"Hamming Distance: {distance}")

