import re

TRANSLATION = {
    'Methionine': ('AUG'),
    'Phenylalanine': ('UUU', 'UUC'),
    'Leucine': ('UUA', 'UUG'),
    'Serine': ('UCU', 'UCC', 'UCA', 'UCG'),
    'Tyrosine': ('UAU', 'UAC'),
    'Cysteine': ('UGU', 'UGC'),
    'Tryptophan': ('UGG')
}

STOP_CODONS = ('UAA', 'UAG', 'UGA')

def proteins(strand):
    polypeptide = []

    codons = re.findall('...', strand)
    for codon in codons:
        for protein in TRANSLATION:
            if codon in TRANSLATION.get(protein):
                polypeptide.append(protein)
            elif codon in STOP_CODONS:
                return polypeptide
    
    return polypeptide
