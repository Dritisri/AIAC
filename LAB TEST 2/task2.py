import csv
import io

# Sensitive columns to redact
PII_COLUMNS = {'name', 'email', 'phone'}

# Sample input as string (simulate file)
input_csv = """name,email,dept,salary
Raj,raj@example.com,Eng,120
Maya,maya@example.com,HR,90
"""

# Read input CSV
input_file = io.StringIO(input_csv)
reader = csv.DictReader(input_file)
output = io.StringIO()
writer = csv.DictWriter(output, fieldnames=reader.fieldnames)
writer.writeheader()

for row in reader:
    for col in PII_COLUMNS:
        if col in row:
            row[col] = 'REDACTED'
    writer.writerow(row)

# Print output CSV
print(output.getvalue())