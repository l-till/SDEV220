import os
import csv

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'books2.csv')

# Read books.csv using DictReader
with open(file_path, newline='', encoding='utf-8') as csvfile:
    books = list(csv.DictReader(csvfile))

# Print the values
for book in books:
    print(book)
