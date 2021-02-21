#Rumman-Al-Karim
#This program allows the user to enter a dna string 
def comp_dna(dna):
    """
    A <-> T   &  C <-> G

    Output: [('A', 'T'), ('C', 'G'), etc...]
    """

    {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'} 

    if type(dna) == list: 
        dna = ''.join(dna)
    
    dna = dna.upper()
    helix = [] 
    str2 = '' 

    for i in dna: 
        helix.append((i, convs[i])) 
        str2 += i

    return helix, str2 
  
  
dna = [('CTTAGTTC'),('GGGTAACCT')] 
# [('C', 'G'), ('T', 'A'), ('T', 'A'), ('A', 'T'), ('G', 'C'), ('T', 'A'), ('T', 'A'), ('C', 'G')]



dna = list(dna)  
str2, helix = comp_dna(dna)
print(helix)
print(str2)
