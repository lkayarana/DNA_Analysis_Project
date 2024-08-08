# DNA Analysis Project

This project performs various bioinformatics analyses on a DNA sequence and visualizes the results. The project includes motif searching, GC content calculation, nucleotide frequency determination, and simple mutation analysis. Results are displayed both textually and graphically.



## Installation

1. Clone or download the project folder to your computer.
2. Open a terminal or command line and navigate to the project folder.
3. Run the `scripts/dna_analysis.py` script:

```bash
python scripts/dna_analysis.py
```


## Usage

When the program is run, it prompts the user for a DNA sequence, a motif to search for, and a mutation to search for.

## Example Input

Please enter the DNA sequence: ATGCGATATGCGTACGTAGCTAGCTAGCGTATCGATCG
Please enter the motif to search for: ATG
Please enter the mutation to search for: TCG



## Example Output

Motif Locations:
[0, 7, 18]

Motif Visualized:
ATG    ATG           ATG              

GC Content:
44.44%

Nucleotide Frequency:
{'A': 9, 'T': 9, 'G': 10, 'C': 8}

Mutation Locations:
[5, 29]


## Graphical Outputs

1. GC Content Graph

2. Nucleotide Frequency Graph


## Functions

### Input Handling
 - dna_input(): Prompts the user for the DNA sequence.
 - motif_input(): Prompts the user for the motif to search for.
 - mutation_input(): Prompts the user for the mutation to search for.

## Motif Searching
 - search_motif(dna, motif): Searches for the motif in the DNA sequence and returns the positions as a list.

## GC Content Calculation
 - calculate_gc_content(dna): Calculates the GC content of the DNA sequence and returns the percentage.

## Nucleotide Frequency
 - calculate_nucleotide_frequency(dna): Calculates the frequency of each nucleotide in the DNA sequence and returns a dictionary.

## Mutation Analysis
 - search_mutation(dna, mutation): Searches for the mutation in the DNA sequence and returns the positions as a list.

## Output Handling
 - display_result(result, title): Prints the analysis results to the screen.

## Visualization
 - visualize_motif(dna, motif_positions, motif): Visualizes the positions of the motif in the DNA sequence.
 - plot_gc_content(gc_content): Creates a bar plot for GC content.
 - plot_nucleotide_frequency(frequency): Creates a bar plot for nucleotide frequency.


## Results
Analysis results are saved in the results/ folder and can be accessed from there.
 - `gc_content.png`: Graph of GC content.
 - `nucleotide_frequency.png`: Graph of nucleotide frequencies.


