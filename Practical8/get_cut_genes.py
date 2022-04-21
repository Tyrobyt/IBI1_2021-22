#2. Identify those genes whose sequences can be cut by EcoRI
#2.1 create a script file name get_cut_genes.py
#input: the gene name and the length of DNA sequence
#output: identify sequences which can be cut by EcoRI and simplify the sequence name
# Output results in a new fasta file : cut_genes.fa
# aim: able to read the original fasta and create a new file
# new file: cut_genes.fa with sequence of genes that contain sequences that can be cut by EcoRI
import re
# To read the fasta, we use open()
all_dna=open(r"C:\Users\Tyrobyt\Desktop\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")#read the fasta file which is stored in my desktop
#make a dict
seqs={}
#store the data of sequence in dict
for line in all_dna:
    if line.startswith('>'):
        #remove the \n
        line = line.replace('\n', '')
        #remove the '>'
        seq_name = line[1:]#let the information be the name of sequence
    else:
        line = line.replace('\n', '')  # join the sequence together
        seqs[seq_name]=line #add value to dict

all_dna.close()


#the cutting site of EcoRI is GAATTC (https://www.biomart.cn/experiment/430/457/741/43956.htm)
a='GAATTC'
#find the sequence in dict which can be cut by EcoRI and store them in a new dict
#list the line number of sequence
count=0
EcoRI_sequence={}
for (key,value) in zip(seqs.keys(),seqs.values()):
    count=count+1
    if value.find(a)>=0:
        key=key+"   "+str(count)+"      "
        EcoRI_sequence[key]=value


#turn the dict into str
newdata=str(EcoRI_sequence)
print(newdata)
print(type(newdata))
#select the name of sequence
name=re.findall(r'gene:(\S+)',newdata)
#select the code of sequence
sequence=re.findall(r'[A-Z]+GAATTC[A-Z]+',newdata)
#select the number of sequence
#use .*?
num=re.findall(r'   .*?      ',newdata)

#store selected data in newfile
#name,sequence,name are list, we should turn it into str
file=open(r'C:\Users\Tyrobyt\Desktop\cut_genes.fa','w')#the out put file is created in my desktop
for i in range(0,len(sequence)):
    line1=str(name[i])+str(num[i])
    line2=str(sequence[i])
    file.write('>'+line1+'\n'+line2+'\n')

file.close()
