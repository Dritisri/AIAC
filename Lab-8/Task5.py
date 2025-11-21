def convert_date_format(date_str):
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Input date must be in 'YYYY-MM-DD' format.")
    year, month, day = parts
    return f"{day}-{month}-{year}"
# Test cases1:
print(convert_date_format("2023-10-05"))  # Output: "05-10-2023"
# Test cases2:
print(convert_date_format("1999-01-15"))  # Output: "15-01-1999"