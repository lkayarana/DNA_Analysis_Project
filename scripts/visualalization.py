import matplotlib.pyplot as plt

def motif_visualization(dna, motif_found_positions, motif):
    if not motif_found_positions:
        print("Görselleştirme için herhangi bir motif bulunamadı.")
        return

    dna_length = len(dna)
    visual = [' '] * dna_length

    for position in motif_found_positions:
        for i in range(len(motif)):
            visual[position + i] = motif[i]

    visual_str = ''.join(visual)
    print("DNA Dizisi:")
    print(dna)
    print("\nMotifin Bulunduğu Konumlar:")
    print(visual_str)

def gc_content_graph(gc_content):
    plt.figure()
    plt.bar(['GC İçeriği'], [gc_content])
    plt.ylabel('Yüzde (%)')
    plt.title('GC İçeriği')
    plt.show()

def nukleotide_frequency_graph(frequency):
    plt.figure()
    plt.bar(frequency.keys(), frequency.values())
    plt.ylabel('Sayı')
    plt.title('Nükleotid Frekansı')
    plt.show()
