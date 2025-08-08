# gc_at_from_fasta.py
# Reads DNA sequence from a FASTA file,
# calculates GC and AT content


import sys

def read_fasta(file_path):
    """Reads a FASTA file and returns the sequence as a single string."""
    sequence = ""
    with open(file_path, "r") as file:
        for line in file:
            if not line.startswith(">"):  # Ignore header lines
                sequence += line.strip().upper()
    return sequence

def calculate_gc_at(sequence):
    """Calculates GC and AT content percentages."""
    length = len(sequence)
    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = ((g_count + c_count) / length) * 100
    at_content = ((a_count + t_count) / length) * 100

    return length, a_count, t_count, gc_content, at_content

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gc_at_from_fasta.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    sequence = read_fasta(fasta_file)
    length, a_count, t_count, gc_content, at_content = calculate_gc_at(sequence)

    print(f"Length: {length}")
    print(f"A count: {a_count}")
    print(f"T count: {t_count}")
    print(f"GC Content: {gc_content:.2f}%")
    print(f"AT Content: {at_content:.2f}%")

