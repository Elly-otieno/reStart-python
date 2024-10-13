'''
Working with the string sequence and Numeric weight of Insulin in python
'''

# Store the human prepoinsulin sequence in a variable called prepoinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"


# store the remaining sequence elements of human insulin in variables:

isInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = 	"giveqcctsicslyqlenycn"
cInsulin = 	"rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin
print(insulin)

# printing "the sequence of human insulin" to console using successive print() commands:

print("The sequence of human preproinsulin:")

print(preproInsulin)

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)

print("The sequence of human insulin, chain a: ", aInsulin)


# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
    'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
    'V': 117.15, 'W': 204.23, 'Y': 181.19
} 

# Count the number of each amino acids  
# aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
# 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
# 'V', 'W', 'Y']})  

amino_acids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 
               'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 
               'W', 'Y']

aaCountInsulin = {}

for aa in amino_acids:
    count = float(insulin.upper().count(aa))   #convert to uppercase and count occurences
    
    aaCountInsulin[aa] = count
    

# Multiply the count by the weights  
# molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
# ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
# 'S', 'T', 'V', 'W', 'Y']}.values())  

rough_molecular_weight = 0.0   #initialize

for aa in amino_acids:
    count = aaCountInsulin[aa]  #retrieve count
    
    weight = aaWeights[aa]  #get weight of each aa
    
    new_weight = count * weight
    
    rough_molecular_weight += new_weight
    

print("The rough molecular weight of insulin: " + str(rough_molecular_weight))


molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((rough_molecular_weight - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))