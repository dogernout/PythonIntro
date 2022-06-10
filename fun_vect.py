def superposition(funmod, funseq):
    return [(lambda x, f = funelement: funmod(f(x))) for funelement in funseq]
