# GC & AT Content Calculator with Plot and CSV Export

This Python project reads a DNA sequence from a FASTA file, calculates GC and AT content percentages, exports the results to a CSV file, 
and displays a bar plot for easy visualization.

---

## What is GC and AT Content?

DNA is made up of four bases:  
- Adenine (A)  
- Thymine (T)  
- Guanine (G)  
- Cytosine (C)  

**GC content** is the percentage of bases in the DNA sequence that are either G or C.  
**AT content** is the percentage that are A or T.

### Formulas:

GC Content  = ((G + C)\length) * 100

AT Content =  ((A + T)/length) * 100

## How to Use

1. Make sure Python is installed.  
2. Install the plotting library by running this in the terminal:  
   
   pip install matplotlib 

   Places the FASTA file in the project folder (e.g., example_sequence.fasta.txt)

Run the script from the terminal:

python gc_content_plot_export.py example_sequence.fasta.txt

The script will:
Print the counts and percentages.
Save the results to gc_at_content_results.csv.
Display a bar plot of GC and AT content.

## Plot Explanation
The script uses the matplotlib library to create a bar plot that visually compares the GC content and AT content percentages. This helps to quickly understand the composition of your DNA sequence in a clear and graphical way.

The x-axis shows the categories: GC Content and AT Content.
The y-axis shows their corresponding percentages.
Bars are colored green (GC) and orange (AT) for easy differentiation.
The y-axis scale is fixed from 0 to 100 (%) to represent percentage values.
