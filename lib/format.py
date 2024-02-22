
"""
Functions for formatting input files or data
"""

import sys

def format_region(region_string):
    if ":" in region_string and "-" not in region_string or ":" not in region_string and "-" in region_string:
        sys.exit(f"Error: region {region_string} should be formated as 'chr' or 'chr:start-stop'")
    if ":" in region_string and "-" in region_string:
        chrom = region_string.split(":")[0]
        start = region_string.split(":")[1].split("-")[0]
        stop  = region_string.split(":")[1].split("-")[1]
        return (chrom, int(start), int(stop))
    else:
        chrom = region_string
        return (chrom, None, None)
assert format_region("seqA") ==      ("seqA", None, None)
assert format_region("seqA:1-10") == ("seqA", 1, 10)

def extract(seq, start, stop):
    return seq[start:stop]
assert extract("ATCGATCG", None, None) == "ATCGATCG"
assert extract("ATCGATCG", 0,    3) ==    "ATC"

def trim_name(name):
    return name.split(" ")[0]

