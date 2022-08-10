dna = ['G', 'C', 'T', 'A']
rna = ['C', 'G', 'A', 'U']

def to_rna(dna_strand):
    conversion_str = ''

    for dna_nucleotide in list(dna_strand):
        index = dna.index(dna_nucleotide)
        rna_nucleotide = rna[index]
        conversion_str += rna_nucleotide

    return conversion_str