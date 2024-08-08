def motif_search(dna, motif):
    motif_found_positions = []
    for i in range(len(dna) - len(motif) + 1):
        if dna[i:i+len(motif)] == motif:
            motif_found_positions.append(i)
    return motif_found_positions