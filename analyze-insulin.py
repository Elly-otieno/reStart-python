'''
Preparing to analyze insulin with python
'''

import re

with open('preproinsulin-seq.txt', 'r') as file:
    myTxt = file.read()

cleanedTxt = re.sub(r'\d+|ORIGIN|//|\s+', '', myTxt)

print(len(cleanedTxt))


with open('preproinsulin-seq-clean.txt', 'w') as output_file:
    output_file.write(cleanedTxt)
    
 
 
with open('insulin-seq-clean.txt', 'w') as amino_output_file:
    amino_output_file.write(cleanedTxt[:24])
    
    
print(cleanedTxt[:24])
print(len(cleanedTxt[:24]))

with open('binsulin-seq-clean.txt', 'w') as bi_amino_file:
    bi_amino_file.write(cleanedTxt[24:54])
    
print(cleanedTxt[24:54])
print(len(cleanedTxt[24:54]))

with open('cinsulin-seq-clean.txt', 'w') as c_amino_file:
    c_amino_file.write(cleanedTxt[54:89])
    
print(cleanedTxt[54:89])
print(len(cleanedTxt[54:89]))

with open('ainsulin-seq-clean.txt', 'w') as a_amino_file:
    a_amino_file.write(cleanedTxt[89:])
    
print(cleanedTxt[89:])
print(len(cleanedTxt[89:]))