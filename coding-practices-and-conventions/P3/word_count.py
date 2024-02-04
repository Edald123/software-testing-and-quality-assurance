"""
This script processes a single file passed by the user as a command-line argument. 
It identifies all distinct words and their frequency in the file and writes the 
results to a text file named 'word_count_results.txt'.
"""

import argparse
import time
import locale

def count_words(file):
    """Count the frequency of each word in the file."""
    word_count = {}
    with open(file, 'r', encoding=locale.getencoding()) as f:
        for line_number, line in enumerate(f, start=1):
            try:
                words = line.strip().split()
                for word in words:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
            except (UnicodeDecodeError, ValueError) as e:
                print(f"An error occurred on line {line_number}: {e}")
    return word_count

def print_and_write_table(word_count, file):
    """Print the word count results in a tabular form and write them to a file."""
    results = [["Word", "Count"]]
    sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_word_count:
        results.append([word, str(count)])

    widths = [max(map(len, col)) for col in zip(*results)]
    for row in results:
        line = "  ".join((val.ljust(width) for val, width in zip(row, widths)))
        print(line)
        file.write(line + '\n')
        line = "-" * (sum(widths) + len(widths) * 2)
        print(line)
        file.write(line + '\n')

def main(file):
    """Process the file and count word frequencies."""
    start_time = time.time()

    word_count = count_words(file)

    # Print and write results to a file
    with open('word_count_results.txt', 'w', encoding=locale.getencoding()) as f:
        print_and_write_table(word_count, f)
        elapsed_time = time.time() - start_time
        print(f"Time taken: {elapsed_time} seconds")
        f.write(f"\nTime taken: {elapsed_time} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some file.')
    parser.add_argument('file', type=str, help='The file to be processed')

    args = parser.parse_args()

    main(args.file)
