import sqlite3
from sqlalchemy import create_engine, MetaData, select

conn = sqlite3.connect("books.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

books_data = [
    ("The Weirdstone of Brisingamen", "Alan Garner", 1960),
    ("Perdido Street Station", "China Miéville", 2000),
    ("Thud!", "Terry Pratchett", 2005),
    ("The Spellman Files", "Lisa Lutz", 2007),
    ("Small Gods", "Terry Pratchett", 1992)
]

c.execute("SELECT COUNT(*) FROM books")
if c.fetchone()[0] == 0:
    c.executemany("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", books_data)
    conn.commit()

conn.close()

engine = create_engine('sqlite:///books.db')
metadata = MetaData()
metadata.reflect(bind=engine)

books = metadata.tables['books']

stmt = select(books.c.title).order_by(books.c.title)


with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(row.title)