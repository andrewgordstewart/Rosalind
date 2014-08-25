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
