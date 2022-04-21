#1.restriction fragment length counter
#name fragment_counter.py
seq ='ATGCAATCGACTACGATCAATCGAGGGCC'
#count the number of cut
cut= seq.count('^')
#the number of fragment equals to the number of cut + 1
fragment=cut+1
#print the outcome
print(fragment)
