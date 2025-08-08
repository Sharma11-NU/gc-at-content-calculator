# gc_at_from_fasta.py
# Reads DNA sequence from a FASTA file,
# calculates GC and AT content and gives a plot

import sys
import csv
import matplotlib.pyplot as plt

def read_fasta(file_path):
    sequence = ""
    with open(file_path, "r") as file:
        for line in file:
            if not line.startswith(">"):
                sequence += line.strip().upper()
    return sequence

def calculate_gc_at(sequence):
    length = len(sequence)
    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = ((g_count + c_count) / length) * 100
    at_content = ((a_count + t_count) / length) * 100

    return length, a_count, t_count, gc_content, at_content

def export_to_csv(filename, length, a_count, t_count, gc_content, at_content):
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Metric', 'Value'])
        writer.writerow(['Length', length])
        writer.writerow(['A count', a_count])
        writer.writerow(['T count', t_count])
        writer.writerow(['GC Content (%)', f"{gc_content:.2f}"])
        writer.writerow(['AT Content (%)', f"{at_content:.2f}"])

def plot_gc_at(gc_content, at_content):
    categories = ['GC Content', 'AT Content']
    values = [gc_content, at_content]

    plt.bar(categories, values, color=['green', 'orange'])
    plt.title('GC and AT Content (%)')
    plt.ylabel('Percentage (%)')
    plt.ylim(0, 100)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gc_content_plot_export.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    seq = read_fasta(fasta_file)
    length, a_count, t_count, gc_content, at_content = calculate_gc_at(seq)

    print(f"Length: {length}")
    print(f"A count: {a_count}")
    print(f"T count: {t_count}")
    print(f"GC Content: {gc_content:.2f}%")
    print(f"AT Content: {at_content:.2f}%")

    # Export to CSV
    export_to_csv('gc_at_content_results.csv', length, a_count, t_count, gc_content, at_content)
    print("Results exported to gc_at_content_results.csv")

    # Plot the results
    plot_gc_at(gc_content, at_content)
