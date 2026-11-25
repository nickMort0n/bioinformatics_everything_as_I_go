Nucleotides = ["A", "C", "T", "G"]

def isValid(strand):
    holder = strand.upper() #turns everything in the strand to an uppercase strand

    for base in holder:
        if base not in Nucleotides:
            return False

    return True