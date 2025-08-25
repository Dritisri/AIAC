import csv

def analyze_csv(filename):
    total_rows = 0
    empty_rows = 0
    total_words = 0

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_rows += 1
            # Check if all fields are empty or whitespace
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            # Count words in non-empty cells
            for cell in row:
                words = cell.strip().split()
                total_words += len(words)

    return total_rows, empty_rows, total_words

# Example usage:
rows, empty, words = analyze_csv('filename.csv')
print(f"Total Rows: {rows}")
print(f"Empty Rows: {empty}")
print(f"Total Words: {words}")