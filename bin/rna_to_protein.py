f = open('../data/rna_to_codon_table.txt', 'r')



strip = lambda s: s.strip()
parse = lambda s: map(strip, s.split(", "))

line = f.readline()
table = []

while line:
    table.append(line)
    line = f.readline()

table = map(parse, table)


for a in table:
    a[0] = 'key: ' + a[0]
    print a
