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



#SURPRISE TASKS


# (PART A) A to B
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Normalized counts for HBR vs URH
data_source1 = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/hbr_uhr_top_deg_normalized_counts.csv"
# extract data from data source
df = pd.read_csv(data_source1)

df.columns = ['genes', 'HBR_1', 'HBR_2', 'HBR_3', 'UHR_1', 'UHR_2', 'UHR_3']
df.set_index("genes", inplace=True)

# heatmap
sns.clustermap(
    df,
    cmap="Blues",
    figsize=(4,4),
    linewidths=0.5,
    linecolor="black")

# Differential expression results (chromosome 22) (b)
data_source2 = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/hbr_uhr_deg_chr22_with_significance.csv"
# extract data from data source
df1 = pd.read_csv(data_source2)

# volcano plot
plt.figure(figsize=(4,4))
sns.scatterplot(df1, x="log2FoldChange", y="-log10PAdj", hue="significance")
plt.axvline(x=-1, color="grey", linestyle="--", linewidth=1)
plt.axvline(x=1, color="grey", linestyle="--", linewidth=1)
plt.axhline(y=1.3, color="grey", linestyle="--", linewidth=1)
plt.show()


# (PART B) C to F
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_source3 = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/data-3.csv"


# Breast Cancer Wisconsin dataset (c)
# extract data from data source
df21 = pd.read_csv(data_source3)
sns.scatterplot(df21, x="radius_mean", y="texture_mean", hue="diagnosis")



# Correlation Heatmap (d)
# extract data from data source
df2 = pd.read_csv(data_source3)
# compute only the correlation matrix of 6 key features
x = df2[['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean']]

# plot heatmap
sns.heatmap(x.corr(numeric_only=True), annot=True, cmap="Blues")


# Breast Cancer Wisconsin dataset (e)
# extract data from data source
df31 = pd.read_csv(data_source3)

# plot scatterplot
sns.scatterplot(df31, x="smoothness_mean", y="compactness_mean", hue="diagnosis")


# Breast Cancer Wisconsin dataset (f)
# extract data from data source
df61= pd.read_csv(data_source3)

# plot density plot
sns.displot(df61, x="area_mean", kind="kde", hue="diagnosis", fill=True)







