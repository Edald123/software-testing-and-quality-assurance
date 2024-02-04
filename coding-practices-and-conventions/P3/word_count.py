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
        for line in f:
            words = line.strip().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

def print_and_write_results(word_count, file):
    """Print the word count results and write them to a file."""
    for word, count in word_count.items():
        line = f"{word}: {count}"
        print(line)
        file.write(line + '\n')

def main(file):
    """Process the file and count word frequencies."""
    start_time = time.time()

    word_count = count_words(file)

    # Print and write results to a file
    with open('word_count_results.txt', 'w', encoding=locale.getencoding()) as f:
        print_and_write_results(word_count, f)
        elapsed_time = time.time() - start_time
        print(f"Time taken: {elapsed_time} seconds")
        f.write(f"\nTime taken: {elapsed_time} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some file.')
    parser.add_argument('file', type=str, help='The file to be processed')

    args = parser.parse_args()

    try:
        main(args.file)
    except Exception as e:
        print(f"An error occurred: {e}")