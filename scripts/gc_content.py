def gc_content_calculator(dna):
    g = dna.count("G")
    c = dna.count("C")
    gc_content = (g + c) / len(dna) * 100
    return gc_content