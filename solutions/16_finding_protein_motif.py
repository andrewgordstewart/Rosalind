from rosalind.iotools import parse_fasta, get_uniprot
from rosalind.genetools import validate_sequence


def solve(dataset):
    protein_ids = [s.strip() for s in dataset.split()]
    protein_fastas = [get_uniprot(uniprot_id) for uniprot_id in protein_ids]
    pure_proteins = [parse_fasta(protein)[1] for protein in protein_fastas]

    motif = Motif([
        MotifElement(matches=True,  acids={'N'}),
        MotifElement(matches=False, acids={'P'}),
        MotifElement(matches=True,  acids={'S', 'T'}),
        MotifElement(matches=False, acids={'P'}),
    ])

    solutions = []
    for i, protein in enumerate(pure_proteins):
        indices = [idx for idx in motif_index(motif, protein)]
        if indices:
            # Note that Rosalind uses 1-indexed arrays
            indices = " ".join(str(i+1) for i in indices)
            solutions.append(
                f"{protein_ids[i]}\n{indices}"
            )

    return '\n'.join(solutions)


def motif_index(motif, sequence, start=0):
    validate_sequence(sequence, 'protein')

    # print 'checking %s for %s' % (sequence, motif)

    a = len(sequence)
    b = len(motif)

    for i in range(start, a-b):
        if motif.matches(sequence[i:]):
            yield i


class Motif():
    """
    Look for a particular protein motif in a protein sequence.
    - A protein motif is represented by a regular expression as follows:
        [XY] means "either X or Y" and {X} means "any amino acid except X."
        For example, the N-glycosylation motif is written as N{P}[ST]{P}.
    """
    def __init__(self, motif_elements):
        self.motif_elements = motif_elements

    def matches(self, seq):
        return all(
            m.matches(seq[i]) for i, m in enumerate(self.motif_elements)
        )

    def __len__(self):
        return len(self.motif_elements)


class MotifElement():
    """
    :param matches: whether the acid in question should match the
        MotifElement's acids set.
        ie. if the motif element is [SP], then matches should be True
    :param acids: set of amino acid characters indicating which acids to test
    """
    def __init__(self, matches, acids):
        self._matches = matches
        self.acids = acids

    def matches(self, acid):
        """
        :param acid: single character string

        :returns:
            - when _matches is True, whether acid is one of the element's acids
            - when _matches is False, whether acid is not one of the element's
              acids
        """
        if type(acid) != str or len(acid) > 1:
            raise ValueError

        return (
            (self._matches and acid in self.acids) or
            ((not self._matches) and acid not in self.acids)
        )

    def __repr__(self):
        if self._matches and len(self.acids) == 1:
            return f"{list(self.acids)[0]}"
        elif self._matches:
            return f"[{''.join(list(self.acids))}]"
        else:
            return f"{{{''.join(list(self.acids))}}}"
