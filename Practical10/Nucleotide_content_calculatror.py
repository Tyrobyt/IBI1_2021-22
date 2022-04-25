# 1. Nucleotide content calculatror
# input: a single string variable describing a DNA strand
# returns: the percentage of nucleotides in that sequence which made up of  A, T, G, C nucleotides.
# should be capable of processing sequences provided as upper cases(大写), lower cases（小写）, or a mixture of the two as is commonly found in DNA databases.
# should include an example of how this function should be called within your code

# take YBR024_mRNA cdna chromosome as example
dna=input("input:")
input:"ATGTTGAATAGTTCAAGAAAATATGCTTGTCGTTCCCTATTCAGACAAGCGAACGTCTCAATAAAAGGACTCTTTTATAATGGAGGCGCATATCGAAGAGGGTTTTCAACGGGATGTTGTTTGAGGAGTGATAACAAGGAAAGCCCAAGTGCAAGACAACCACTAGATAGGCTACAACTAGGTGATGAAATCAATGAACCAGAGCCTATTAGAACCAGGTTTTTTCAATTTTCCAGATGGAAGGCCACCATTGCTCTATTGTTGCTAAGTGGTGGGACGTATGCCTATTTATCAAGAAAAAGACGCTTGCTAGAAACTGAAAAGGAAGCAGATGCTAACAGAGCTTACGGTTCAGTAGCACTTGGCGGTCCTTTCAATTTAACAGATTTTAATGGTAAGCCTTTCACTGAGGAGAATTTGAAGGGTAAGTTTTCCATTTTATACTTTGGATTCAGTCATTGCCCGACATTTGTCCAGAAGAGCTTGACAGATTAACGTATTGGATTTCTGAATTAGATGATAAAGACCATATAAAGATACAGCCATTGTTTATCTCATGTGATCCTGCAAGAGATACACCGGATGTCTTGAAAGAGTACTTAAGCGATTTTCACCCAGCTATCATTGGTTTAACCGGTACGTACGACCAAGTGAAAAGCGTATGCAAAAAATACAAGGTATATTTTTCAACTCCACGTGATGTCAAGCCCAACCAGGATTACTTAGTGGACCATTCGATATTTTTCTATTTGATCGACCCTGAAGGACAGTTTATCGATGCGTTGGGAAGAAACTACGATGAGCAATCTGGTCTCGAAAAGATTCGTGAACAAATTCAGGCGTATGTGCCAAAGGAAGAACGGGAGCGTAGGTCAAAAAAATGGTACTCTTTTATCTTCAATTGA"
# turn all the letters in dna into uppercases
dna.swapcase()
# count the number of each nucleotides
A=dna.count('A')
T=dna.count('T')
G=dna.count('G')
C=dna.count('C')
sum=A+T+G+C
#calculate the percentage of each nucleotide
a=A/sum*100
t=T/sum*100
g=G/sum*100
c=C/sum*100
# print the outcome
print("the percentage of nucleotide A = "+str(a)+"%")
print("the percentage of nucleotide T = "+str(t)+"%")
print("the percentage of nucleotide G = "+str(g)+"%")
print("the percentage of nucleotide C = "+str(c)+"%")
