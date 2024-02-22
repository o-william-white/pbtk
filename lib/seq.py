"""
Functions for calculating properties of DNA sequences
"""

import sys

# length
def length(seq):
    return (len(seq))
assert length("ATCG") == 4

# at content
def at_content(seq):
    seq = seq.upper()
    return (seq.count("A") + seq.count("T")) / len(seq)
assert at_content("AtCG") == 0.5

# gc content
def gc_content(seq):
    seq = seq.upper()
    return (seq.count("G") + seq.count("C")) / len(seq)
assert at_content("ATCG") == 0.5

# n_content
def n_content(seq):
    seq = seq.upper()
    return (seq.count("N") / len(seq))
assert n_content("NNCG") == 0.5

# base content
def base_content(seq):
    seq = seq.upper()
    list_counts = []
    for b in ["A", "T", "C", "G", "N"]:
        list_counts.append(seq.count(b))
    return list_counts
assert base_content("AATCgNNN") == [2, 1, 1, 1, 3]

# sequence complexity (percentage of bases that are different from their next base)
def sequence_complexity(seq):
    seq = seq.upper()
    previous_base, differences = None, 0
    for base in seq:
        if previous_base == None:
            previous_base = base
        else:
            if base != previous_base:
                differences += 1
                previous_base = base
    complexity = differences / (len(seq)-1)
    return complexity
assert sequence_complexity("ATCGA") == 1.0
assert sequence_complexity("AACAA") == 0.5

# get windows
def get_windows(name, seq, window):
    if len(seq) < window:
        sys.exit(f"Error: {name} is shorter than window size {window}")
    else:
       for i in range(0, len(seq), window):
          start = i
          end   = i + window
          w = seq[start:end]
          yield [name, start, end, w]
assert list(get_windows("seqA", "AAAATTTTGGGGCCCC", 4)) == [["seqA", 0,  4, "AAAA"],
                                                            ["seqA", 4,  8, "TTTT"],
                                                            ["seqA", 8,  12, "GGGG"],
                                                            ["seqA", 12, 16, "CCCC"]]

