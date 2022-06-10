import itertools

def chainslice(begin, end, *seq):
    return itertools.islice(itertools.chain.from_iterable(seq), begin, end)
