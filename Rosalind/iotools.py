import requests


def parse_fasta(fasta_id):
    data = fasta_id.split('\n')
    name = data[0]
    sequence = ''.join(data[1:-1])
    return (name, sequence)


def read_fasta(fasta):
    name, seq = None, []
    for line in fasta.split('\n'):
        line = line.rstrip()
        if line.startswith(">"):
            if name:
                yield (name, ''.join(seq))
            name, seq = line[1:], []
        else:
            seq.append(line)
    if name:
        yield (name, ''.join(seq))


def read_complete_fasta(fp):
    fasta = []
    for name, seq in read_fasta(fp):
        fasta.append((name, seq))

    return fasta


def get_uniprot(uniprot_id):
    url = 'http://www.uniprot.org/uniprot/' + uniprot_id + '.fasta'
    return requests.get(url).text


def copy_to_clipboard(s):
    import os

    cmd = 'echo %s | tr -d "\n" | pbcopy' % s
    os.system(cmd)
