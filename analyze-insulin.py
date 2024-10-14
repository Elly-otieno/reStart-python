'''
Preparing to analyze insulin with python

In information technology, Python works well as the programming language of choice for manipulating strings, sequences, and numbers. 
Python is especially preferred in scientific computing applications such as physics, chemistry, and biology.

In some of the labs for the Python modules, we will perform simple sequence manipulations and calculations on human insulin, which is a well-known hormone in the human body that is responsible for regulating sugars.

In this lab, we will:
 - Retrieve the protein sequence of human insulin from human preproinsulin
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