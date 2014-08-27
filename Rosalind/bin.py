# I'm doing this wrong

def is_dominant_prob(num_homo_dom, num_hetero, num_homo_rec):
    total = num_homo_dom + num_hetero + num_homo_rec
    total = total*(total-1)


    # prob(at least one mate is homo_dom):
    p1 = num_homo_dom*(num_homo_dom-1
                       + 2*num_hetero
                       + 2*num_homo_rec
                       )/float(total)

    # prob(hetero + hetero):
    p2 = num_hetero*(num_hetero-1)/float(total)

    # prob(hetero + homo_rec)
    p3 = 2*num_hetero*num_homo_rec/float(total)

    return p1 + .75*p2 + .5*p3

print is_dominant_prob(2, 2, 2)

print is_dominant_prob(17, 20, 22)


cmd = 'echo %s | tr -d "\n" | pbcopy' % ''
os.system(cmd)

# homo_dom + homo_rec = [1,0]
# homo_dom + homo_dom = [1, 1]
# homo_rec + homo_rec = [0,0]
# homo_dom + hetero = .5[1,1] + .5[1,0]
# homo_rec + hetero = .5 hetero + .5 homo_rec
# hetero + hetero = .25[1,1] + .25[0,0] + .5[1,0]

# prob(homo_dom or hetero) =
#     prob(at least one is homo_dom) + prob(hetero + hetero) * .75 + prob(hetero + homo_rec)*.5
