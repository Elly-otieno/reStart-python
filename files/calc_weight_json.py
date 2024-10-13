'''
Creating file handlers and modules for retrieving information about insulin
'''

#  main program
import jsonFileHandler

data = jsonFileHandler.readJsonFile('files/insulin.json')

if data != "":
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    
    # Calculating the molecular weight of insulin  
    # Getting a list of the amino acid (AA) weights  
    aaWeights = data['weights']
    # Count the number of each amino acids  
    amino_acids = ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']
    
    aaCountInsulin = {}
    
    for aa in amino_acids:
        count = float(insulin.upper().count(aa))
        
        aaCountInsulin[aa] = count
        
    # Initialize molecular weight to 0
    
    molecularWeightInsulin = 0.0
    for aa in amino_acids:
        count = aaCountInsulin[aa]  #retrieve aa count
        
        weight = aaWeights[aa]  #get its count
        
        aa_total_weight = count * weight
        
        molecularWeightInsulin += aa_total_weight   # adding new weight to existing aa weight
        
        
    # aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
    # Multiply the count by the weights  
    # molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
    # ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
    
    print("The rough molecular weight of insulin: " +
    str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

else:
    print("Error. Exiting program")