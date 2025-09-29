import sqlite3

def ensure_db(db_name="test_results.db"):
    """Create SQLite DB and table if not exists, then return connection"""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_run_id TEXT,
            user_email TEXT,
            product_name TEXT,
            quantity INTEGER
        )
    """)

    conn.commit()
    return conn
