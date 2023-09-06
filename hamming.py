
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(amino_code_a != amino_code_b for amino_code_a, amino_code_b in zip(strand_a, strand_b))