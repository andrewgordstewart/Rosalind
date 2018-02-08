import re


def solve(dataset):
    dna_strings = [s.strip() for s in dataset.strip().split("\n")]
    full_sequence, partial_sequence = dna_strings
    matches = re.finditer(f"(?={partial_sequence})", full_sequence)
    indexes = [match.start() for match in matches]
    return " ".join(str(index + 1) for index in indexes)
