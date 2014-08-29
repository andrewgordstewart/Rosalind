def fasta_reader(file, key):
    f = open(file, 'r')
    data = f.readlines()

    print data

def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

def read_complete_fasta(fp):
    fasta = []
    for name, seq in read_fasta(fp):
        fasta.append((name, seq))

    return fasta

def copy_to_clipboard(s):
    import os

    cmd = 'echo %s | tr -d "\n" | pbcopy' % s
    os.system(cmd)

if __name__ == '__main__':

    fasta = []
    with open('../data/test.fasta') as fp:
        for name, seq in read_fasta(fp):
            fasta.append((name, seq))
    print fasta[0][1]

