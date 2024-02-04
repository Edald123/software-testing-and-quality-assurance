"""
This script processes a single file passed by the user as a command-line argument. 
It converts the numbers in the file to binary and hexadecimal base and writes the 
results to a text file named 'conversion_results.txt'.
"""

import argparse
import time
import locale

def decimal_to_binary(n):
    """Convert a decimal number to binary using two's complement 
    for negative numbers."""
    if n == 0:
        return '0'
    bits = []
    if n < 0:  # handle negative numbers
        n = (1 << 10) + n
    while n:
        bits.append(str(n & 1))
        n >>= 1
    return ''.join(bits[::-1])

def decimal_to_hexadecimal(n):
    """Convert a decimal number to hexadecimal using two's complement for 
    negative numbers."""
    if n == 0:
        return '0'
    hex_digits = '0123456789ABCDEF'
    hex_bits = []
    if n < 0:  # handle negative numbers
        n = (1 << 32) + n
    while n:
        hex_bits.append(hex_digits[n & 15])
        n >>= 4
    return ''.join(hex_bits[::-1])\

def print_and_write_table(results, file):
    """Print the results in a tabular form with lines separating the columns and 
    rows and write them to a file."""
    widths = [max(map(len, col)) for col in zip(*results)]
    for row in results:
        line = "  ".join((val.ljust(width) for val, width in zip(row, widths)))
        print(line)
        file.write(line + '\n')
        line = "-" * (sum(widths) + len(widths) * 2)
        print(line)
        file.write(line + '\n')

def main(file):
    """Process the file and convert numbers to binary and hexadecimal."""
    lines = []
    total_lines = 0
    with open(file, 'r', encoding=locale.getencoding()) as f:
        for line in f:
            total_lines += 1
            stripped_line = line.strip()
            try:
                number = int(stripped_line)
                lines.append(number)
            except ValueError:
                print(f"Not a number: {stripped_line}")

    start_time = time.time()
    results = [["Index", "Decimal", "Binary", "Hexadecimal"]]
    for i, number in enumerate(lines):
        results.append([str(i), str(number), decimal_to_binary(number),
                        decimal_to_hexadecimal(number)])

    # Print and write results to a file
    with open('convertion_results.txt', 'w', encoding=locale.getencoding()) as f:
        print_and_write_table(results, f)
        f.write(f"Time taken: {time.time() - start_time} seconds")

    print(f"Time taken: {time.time() - start_time} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some file.')
    parser.add_argument('file', type=str, help='The file to be processed')

    args = parser.parse_args()

    main(args.file)
