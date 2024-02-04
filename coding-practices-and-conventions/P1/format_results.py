"""This script reads a tab-delimited file and writes the data to a CSV file."""
import csv
import locale

# Specify the input and output file paths
INPUT_FILE = 'A4.2.P1.Results.txt'
OUTPUT_FILE = 'formated_results.csv'

# Read the input file and split the lines by tabs
with open(INPUT_FILE, 'r', encoding=locale.getencoding()) as file:
    lines = file.readlines()
    data = [line.strip().split('\t') for line in lines if line.strip()]

# Write the data to the output CSV file
with open(OUTPUT_FILE, 'w', newline='', encoding=locale.getencoding()) as file:
    writer = csv.writer(file)
    writer.writerows(data)

print('Conversion complete!')
