# DNA to protein


dna_blocks = ("AAATTGGCCAGCTTGATCTGATGC")
print(f"DNA sequence: {dna_blocks}")
# transcription: DNA to RNA

rna_blocks = dna_blocks.replace("T", "U")
print(f"RNA sequence: {rna_blocks}")

# translation: RNA to protein
protein_codons = {
    "UUU": "F", "CUU": "L", "AUU": "I",
    "GUU": "V", "UUC": "F", "CUC": "L",
    "AUC": "I", "GUC": "V", "UUA": "L",
    "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M",
    "GUG": "V", "UCU": "S", "CCU": "P",
    "ACU": "T", "GCU": "A", "UCC": "S",
    "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T",
    "GCA": "A", "UCG": "S", "CCG": "P",
    "ACG": "T", "GCG": "A", "UAU": "Y",
    "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G"
}


def codon_to_amino(rna_blocks, protein_codons):
    protein = ""
    for i in range(0, len(rna_blocks), 3):
        codon = rna_blocks[i:i + 3]

        amino_acid = protein_codons[codon]
        protein += amino_acid
        if protein.endswith("Stop"):
            protein = protein[:-4]
    return protein


protein = codon_to_amino(rna_blocks, protein_codons)

print(f"Protein sequence: {protein}")

# Hamming distance:

slack_username = "Oluwafoyinsola"
made_up_name = "Fioninuoluwa"

distance = sum(a != b for a, b in zip(slack_username, made_up_name))
print(f"Slack username: {slack_username}")
print(f"Made up name: {made_up_name}")
print(f"Hamming Distance: {distance}")




