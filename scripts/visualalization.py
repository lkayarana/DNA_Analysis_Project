import matplotlib.pyplot as plt

def motif_visualization(dna, motif_found_positions, motif):
    if not motif_found_positions:
        print("No motif found for visualization..")
        return

    dna_length = len(dna)
    visual = [' '] * dna_length

    for position in motif_found_positions:
        for i in range(len(motif)):
            visual[position + i] = motif[i]

    visual_str = ''.join(visual)
    print("DNA Sequence:")
    print(dna)
    print("\nMotif Positions:")
    print(visual_str)

def gc_content_graph(gc_content):
    plt.figure()
    plt.bar(['GC Content'], [gc_content])
    plt.ylabel('Yüzde (%)')
    plt.title('GC Content')
    plt.savefig('results/gc_content.png')
    plt.show()

def nukleotide_frequency_graph(frequency):
    plt.figure()
    plt.bar(frequency.keys(), frequency.values())
    plt.ylabel('Sayı')
    plt.title('Nükleotid Frequency')
    plt.savefig('results/nucleotide_frequency.png')
    plt.show()
