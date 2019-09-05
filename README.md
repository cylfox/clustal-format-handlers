# Clustal Format Handlers
Scripts made in Python to parse clustal format files.
## Author
- MSR <marcossr@uma.es>
## clustal2image.py
### Description
Reads a clustal file, calculates the conservation and generates a plot with it and a smoother one. Then generates an alignment representation plot. 
### Use
```
clustal2image.py -i <inputfile> -o <outputfolder>
```
---
## consensus_seq.py
### Description
Given a alignment in mafft or clustal format gets a sequence where the nucleotide in each position is the most common nucleotide
### Use
```
consensus_seq.py -i <inputfile> -o <outputfolder> -f <format>
```
---
## mafft2image.py
### Description
Plots a mafft alignment with gapps and colors (not for gigabyte-sized files) and the conservation plot
### Use
```
mafft2image.py -i <inputfile> -o <outputfolder>
```
---
## rep_histogram.py
### Description
Given a BLAST file extracts a histogram image.
### Use
```
rep_histogram.py -index <inputfile> -o <outputfolder>
```
---
## functions.py
### Description
Some auxiliar functions.
### Functions
```
def get_color(nucleotide):
def get_most_common(data, coordinate, repetitions):
def read_mafft(file):
def most_common_nucleotide(sequence):
```
---
## models.py
### Description
Some models for better use of the libraries.
### Models
```python
class MafftFragment:
```
