'''
Finds the locations of 'substring' in 'bigstring'.
'''


def find_substring_locations(bigstring, substring):

    locations = []
    i = bigstring.find(substring)
    marker = 0

    while i != -1:
        locations.append(marker + i + 1)
        bigstring = bigstring[i+1:]         # cut off string up to latest occurance
        marker = marker + i + 1             # position in original string
        i = bigstring.find(substring)

    return locations

if __name__ == '__main__':

    with open('../data/rosalind_subs.txt', 'r') as f:
        bigstring = f.readline().strip()
        substring = f.readline().strip()

    locations = find_substring_locations(bigstring, substring)

    for i in locations:
        print i,
