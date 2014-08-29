import SuffixTree.SuffixTree

s = SuffixTree.SuffixTree()

s.add('hello world', 1)
s.add('otello won', 2)

print dir(SuffixTree.SuffixTree), '\n', '-'*20

print dir(SuffixTree.SuffixNode)

x = s.root()

print x.stree_get_children()
