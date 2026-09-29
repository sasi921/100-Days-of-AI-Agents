import sqlite3
SCHEMA = """
CREATE TABLE IF NOT EXISTS orders (
 id INTEGER PRIMARY KEY, customer TEXT NOT NULL, region TEXT NOT NULL,
 product TEXT NOT NULL, amount REAL NOT NULL, order_date TEXT NOT NULL
);
"""
SAMPLE=[(1,"Acme","West","Agent Kit",1200,"2026-09-01"),(2,"Nova","East","RAG Pack",800,"2026-09-02"),(3,"Acme","West","RAG Pack",500,"2026-09-03"),(4,"Zen","South","Agent Kit",1500,"2026-09-04"),(5,"Nova","East","Eval Suite",700,"2026-09-05")]
def connect(path=":memory:"):
    con=sqlite3.connect(path); con.row_factory=sqlite3.Row; return con
def seed(con):
    con.executescript(SCHEMA)
    if con.execute("SELECT COUNT(*) FROM orders").fetchone()[0]==0:
        con.executemany("INSERT INTO orders VALUES (?,?,?,?,?,?)",SAMPLE); con.commit()
