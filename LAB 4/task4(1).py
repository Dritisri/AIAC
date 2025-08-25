import csv

def analyze_csv(filename='filename.csv'):
    total_rows = 0
    empty_rows = 0
    total_words = 0

    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            total_rows += 1
            # Check if all fields are empty or whitespace
            if all(cell.strip() == '' for cell in row):
                empty_rows += 1
            # Count words in all cells
            for cell in row:
                total_words += len(cell.strip().split())

    return total_rows, empty_rows, total_words

# Example usage:
rows, empty, words = analyze_csv()
print(f"Total rows: {rows}, Empty rows: {empty}, Total words: {words}")