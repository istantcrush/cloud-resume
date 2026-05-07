from fractions import Fraction

def get_rational(repeat_part):
    # Logic: If the repeat is '142857', the denominator is '999999'
    n = len(repeat_part)
    denominator = 10**n - 1
    numerator = int(repeat_part)
    
    result = Fraction(numerator, denominator)
    return result

# Let's test the Magic of 7
sequence = "142857"
print(f"The fraction for 0.{sequence}... is {get_rational(sequence)}")

import sqlite3

# Connect to a database file
connection = sqlite3.connect('math_data.db')
cursor = connection.cursor()

# Create a table
cursor.execute('CREATE TABLE IF NOT EXISTS history (sequence TEXT, fraction TEXT)')

# Save our result
seq = "142857"
frac = "1/7"
cursor.execute('INSERT INTO history VALUES (?, ?)', (seq, frac))

connection.commit()
connection.close()
print("Saved to database successfully!")