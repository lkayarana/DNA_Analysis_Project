import os
from input_handler import dna_input, motif_input, mutation_input
from motif_search import motif_search
from gc_content import gc_content_calculator
from nucleotide_frequency import nucleotide_frequency
from mutation_analysis import mutation_search
from output_handler import display_result
from visualalization import motif_visualization, gc_content_graph, nukleotide_frequency_graph






def main():
    if not os.path.exists('results'):
        os.makedirs('results')


    dna = dna_input()
    motif = motif_input()
    mutation =mutation_input()

    motif_found_positions = motif_search(dna, motif)
    display_result(motif_found_positions, "Motif Positions")
    motif_visualization(dna, motif_found_positions, motif)

    gc_content = gc_content_calculator(dna)
    display_result(gc_content, "GC Content")
    gc_content_graph(gc_content)

    frequency = nucleotide_frequency(dna, mutation)
    display_result(frequency, "Nucleotide Frequency")
    nukleotide_frequency_graph(frequency)

    mutation_found_positions = mutation_search(dna, mutation)
    display_result(mutation_found_positions, "Mutation Positions")


if __name__ == "__main__":
    main()
