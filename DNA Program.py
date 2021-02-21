# Rumman-Al-Karim
# This script allows the user to enter a dna string and 
# return matching base pairs

def comp_dna(dna):
    """
    A <-> T   &  C <-> G
    Example Output: [('A', 'T'), ('C', 'G'), etc...]
    """
    convs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    if type(dna) == list:
        dna = ''.join(dna)

    dna = dna.upper()
    helix = []

    for i in dna:
        helix.append((i, convs[i]))

    return helix
  
  
dna = 'CTTAGTTCGGGTAACCT'
"""
Expected Output:
[('C', 'G'), ('T', 'A'), ('T', 'A'), ('A', 'T'), ('G', 'C'), ('T', 'A'), ('T', 'A'), ('C', 'G')]
"""

dna = list(dna)
helix = comp_dna(dna)
print(helix)
