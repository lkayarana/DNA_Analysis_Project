def mutation_search(dna, mutation):
    mutation_found_positions = []
    for i in range(len(dna) - len(mutation) + 1):
        if dna[i:i+len(mutation)] == mutation:
            mutation_found_positions.append(i)
    return mutation_found_positions