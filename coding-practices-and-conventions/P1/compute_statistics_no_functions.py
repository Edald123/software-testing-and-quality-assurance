"""
This script processes a single file passed by the user as a command-line argument. 
It computes several statistical measures (without using built in functions or modules)
on the data in the file and writes the results to a text file named 'results.txt'.
"""

import argparse
import time
import locale

def calculate_sum(numbers):
    """Return the sum of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_length(numbers):
    """Return the length (number of elements) of a list."""
    length = 0
    for _ in numbers:
        length += 1
    return length

def mean(numbers):
    """Return the mean of a list of numbers."""
    return calculate_sum(numbers) / calculate_length(numbers)

def median(numbers):
    """Return the median of a list of numbers."""
    numbers = sorted(numbers)
    length = calculate_length(numbers)
    middle = length // 2
    if length % 2 == 0:
        return (numbers[middle - 1] + numbers[middle]) / 2
    return numbers[middle]

def mode(numbers):
    """Return the mode of a list of numbers."""
    frequency = {}
    for num in numbers:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1
    max_frequency = 0
    for num, freq in frequency.items():
        if freq > max_frequency:
            max_frequency = freq
            my_mode = num
    if max_frequency == 1:
        return "No mode"
    return my_mode

def standard_deviation(numbers):
    """Return the standard deviation of a list of numbers."""
    avg = mean(numbers)
    my_variance = 0
    for num in numbers:
        my_variance += (num - avg) ** 2
    my_variance /= calculate_length(numbers)
    return my_variance ** 0.5

def variance(numbers):
    """Return the variance of a list of numbers."""
    avg = mean(numbers)
    my_variance = 0
    for num in numbers:
        my_variance += (num - avg) ** 2
    my_variance /= calculate_length(numbers)
    return my_variance

def main(file):
    """Process the file and compute descriptive statistics."""
    lines = []
    total_lines = 0
    with open(file, 'r', encoding=locale.getencoding()) as f:
        for line in f:
            total_lines += 1
            stripped_line = line.strip()
            try:
                number = float(stripped_line)
                lines.append(number)
            except ValueError:
                print(f"Not a number: {stripped_line}")

    start_time = time.time()
    results = [
        f"Total lines: {total_lines}",
        f"Valid lines: {calculate_length(lines)}",
        f"Mean: {mean(lines)}",
        f"Median: {median(lines)}",
        f"Mode: {mode(lines)}",
        f"Standard Deviation: {standard_deviation(lines)}",
        f"Variance: {variance(lines)}",
        f"Time taken: {time.time() - start_time} seconds"
    ]

    # Print and write results to a file
    for result in results:
        print(result)

    with open('results.txt', 'w', encoding=locale.getencoding()) as f:
        for result in results:
            f.write(result + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some file.')
    parser.add_argument('file', type=str, help='The file to be processed')

    args = parser.parse_args()

    main(args.file)
