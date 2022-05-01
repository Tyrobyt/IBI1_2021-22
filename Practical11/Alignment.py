#import the sequence data
import os
import pandas as pd
import re
mouse=open(r"C:\Users\Tyrobyt\Desktop\practical11\DLX5_mouse.fa")
human=open(r"C:\Users\Tyrobyt\Desktop\practical11\DLX5_human.fa")
random=open(r"C:\Users\Tyrobyt\Desktop\practical11\RandomSeq(1).fa")
file_path=r'C:\Users\Tyrobyt\Desktop\practical11\BLOSUM.xlsx'
BLOSUM=pd.read_excel(file_path,header=0)

#make a dict
seqs_mouse={}
seqs_human={}
seqs_random={}
#store the data of sequence in dict
for line in mouse:
    if line.startswith('>'):
        #remove the \n
        line = line.replace('\n', '')
        #remove the '>'
        seq_name = line[1:]#let the information be the name of sequence
    else:
        line = line.replace('\n', '')  # join the sequence together
        seqs_mouse[seq_name]=line #add value to dict

mouse.close()

for line in human:
    if line.startswith('>'):
        #remove the \n
        line = line.replace('\n', '')
        #remove the '>'
        seq_name = line[1:]#let the information be the name of sequence
    else:
        line = line.replace('\n', '')  # join the sequence together
        seqs_human[seq_name]=line #add value to dict

human.close()

for line in random:
    if line.startswith('>'):
        #remove the \n
        line = line.replace('\n', '')
        #remove the '>'
        seq_name = line[1:]#let the information be the name of sequence
    else:
        line = line.replace('\n', '')  # join the sequence together
        seqs_random[seq_name]=line #add value to dict

random.close()

#select the sequence data of protein through value() function
for i in seqs_mouse.values():
    mouse=str(i)
for a in seqs_human.values():
    human=str(a)
for v in seqs_random.values():
    random=str(v)

edit_distance1=0
edit_distance2=0
edit_distance3=0
for i in range(len(mouse)):#compare each amino acid
    if mouse[i]!=human[i]:
        edit_distance1+=1 #add a score 1 if amino acids are different
    if mouse[i]!=random[i]:
        edit_distance2+=1#add a score 1 if amino acid are different
for i in range(len(human)): #compare the human amino acid with random data
    if human[i]!=random[i]: #add a score 1 if amino acid are different
        edit_distance3+=1


# Output:
# 1. print the name, sequence
print("The Name and Sequence of Protein")
print("mouse = "+str(seqs_mouse))
print("human = "+str(seqs_human))
print("random = "+str(seqs_random))

# 2. print the score
# add defination to the distance score
print("\n"+"SCORE"+"\n"+"1 score represents the difference between one corresponding protein sequence")
print("mouse vs human: "+"Score = "+str(edit_distance1))
print("mouse vs random: "+"Score = "+str(edit_distance2))
print("human vs random: "+"Score = "+str(edit_distance3))

# 3. print the identical amino acid for each comparision
print('\n'+"the Percentage of Identical Amino Acids")
print("mouse vs human = "+str((len(mouse)-edit_distance1)/len(mouse)*100)+"%")
print("mouse vs random = "+str((len(mouse)-edit_distance2)/len(mouse)*100)+"%")
print("human vs random = "+str((len(mouse)-edit_distance3)/len(mouse)*100)+"%")
