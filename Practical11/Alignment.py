#import the sequence data
import os
import pandas as pd
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
print("Name and Sequence of Protein")
print("mouse = "+str(seqs_mouse))
print("human = "+str(seqs_human))
print("random = "+str(seqs_random))

# 2. print the score of distance
# add defination to the distance score
print("\n"+"Distance Score"+"\n"+"1 score represents the difference between one corresponding protein sequence")
print("mouse vs human: "+"Distance Score = "+str(edit_distance1))
print("mouse vs random: "+"Distance Score = "+str(edit_distance2))
print("human vs random: "+"Distance Score = "+str(edit_distance3))

# 3. print the identical amino acid for each comparision
print('\n'+"Percentage of Identical Amino Acids")
print("mouse vs human = "+str((len(mouse)-edit_distance1)/len(mouse)*100)+"%")
print("mouse vs random = "+str((len(mouse)-edit_distance2)/len(mouse)*100)+"%")
print("human vs random = "+str((len(mouse)-edit_distance3)/len(mouse)*100)+"%")

# 4.print the score of BLOSUM62
amino = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X',' ']
blosum = [
[ 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
[-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
[-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
[-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[ 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
[-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4],
[-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4],
[-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4],
[-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4],
[-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4],
[-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4],
[-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4],
[-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4],
[-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4],
[ 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4],
[ 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4],
[-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4],
[-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4],
[ 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4],
[-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1, -4],
[-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4],
[ 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1, -4],
[-4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4,  1],
]
# BLOSUM62 matrix from https://blog.csdn.net/laixiangwei/article/details/105831376
score1=0
score2=0
score3=0
c=[]
d=[]
e=[]
for i in mouse:
    a=amino.index(i) # list.index() 用于找出一个元素在列表中的索引位置
    a1=blosum[a] # locate the line in blosum
    for j in human:
        b=amino.index(j)
    c.append(a1[b])# c stores the score of each amino comparison
for k in c:
    score1=score1+c[k] # the sum of element in c is the BLOSUM score

for i in mouse:
    a=amino.index(i) # list.index() 用于找出一个元素在列表中的索引位置
    a1=blosum[a] # locate the line in blosum
    for j in random:
        b=amino.index(j)
    d.append(a1[b])# a[b] locates the final value of comparison; c stores the score of each amino comparison
for k in d:
    score2=score2+d[k] # the sum of element in c is the BLOSUM score

for i in human:
    a=amino.index(i) # list.index() 用于找出一个元素在列表中的索引位置
    a1=blosum[a] # locate the line in blosum
    for j in random:
        b=amino.index(j)
    e.append(a1[b])# c stores the score of each amino comparison
for k in e:
    score3=score3+e[k] # the sum of element in c is the BLOSUM score

print("\n"+"Score of BLOSUM62")
print("mouse VS human = "+str(score1))
print("mouse VS random = "+str(score2))
print("human VS random = "+str(score3))
