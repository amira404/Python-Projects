# multiplication_table.py

def print_multiplication_tables(n):
    for num in range(1, n + 1):
        for x in range(1, num + 1):
            print(num, "x", x, "=", num * x)

def generate_multiplication_table(n):
    table = []
    for num in range(1, n + 1):
        row = []
        for x in range(1, num + 1):
            row.append(num * x)
        table.append(row)
    return table
