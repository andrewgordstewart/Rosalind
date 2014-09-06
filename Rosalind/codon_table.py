def codon_table(with_stops = False):
    table = {'GUC': 'V',
            'ACC': 'T',
            'GUA': 'V',
            'GUG': 'V',
            'GUU': 'V',
            'AAC': 'N',
            'CCU': 'P',
            'UGG': 'W',
            'AGC': 'S',
            'AUC': 'I',
            'CAU': 'H',
            'AAU': 'N',
            'AGU': 'S',
            'ACU': 'T',
            'CAC': 'H',
            'ACG': 'T',
            'CCG': 'P',
            'CCA': 'P',
            'ACA': 'T',
            'CCC': 'P',
            'GGU': 'G',
            'UCU': 'S',
            'GCG': 'A',
            'UGC': 'C',
            'CAG': 'Q',
            'GAU': 'D',
            'UAU': 'Y',
            'CGG': 'R',
            'UCG': 'S',
            'AGG': 'R',
            'GGG': 'G',
            'UCC': 'S',
            'UCA': 'S',
            'GAG': 'E',
            'GGA': 'G',
            'UAC': 'Y',
            'GAC': 'D',
            'GAA': 'E',
            'AUA': 'I',
            'GCA': 'A',
            'CUU': 'L',
            'GGC': 'G',
            'AUG': 'M',
            'CUG': 'L',
            'CUC': 'L',
            'AGA': 'R',
            'CUA': 'L',
            'GCC': 'A',
            'AAA': 'K',
            'AAG': 'K',
            'CAA': 'Q',
            'UUU': 'F',
            'CGU': 'R',
            'CGA': 'R',
            'GCU': 'A',
            'UGU': 'C',
            'AUU': 'I',
            'UUG': 'L',
            'UUA': 'L',
            'CGC': 'R',
            'UUC': 'F'
           }

    return table

      # stops = {'UAA', ''}

def reverse_codon_table():
      table = codon_table()
      reverse_table = {}
      for codon in table:
            reverse_table[table[codon]] = []

      for codon in table:
            reverse_table[table[codon]].append(codon)
      return reverse_table

if __name__ == '__main__':
      print codon_table()
      print '-'*79
      print reverse_codon_table()
