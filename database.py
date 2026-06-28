import sqlite3

DB_NAME = "database/legal.db"

def create_tables():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT,
        category TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        complaint TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_chat(question, answer, category):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO chat_history
    (question, answer, category)
    VALUES (?, ?, ?)
    """, (question, answer, category))

    conn.commit()
    conn.close()


def get_dashboard_data():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM chat_history")
    total_queries = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*) FROM chat_history
    WHERE category='Property Dispute'
    """)
    property_count = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*) FROM chat_history
    WHERE category='Consumer Complaint'
    """)
    consumer_count = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*) FROM chat_history
    WHERE category='Cybercrime'
    """)
    cybercrime_count = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*) FROM chat_history
    WHERE category='Government Services'
    """)
    government_count = cursor.fetchone()[0]

    cursor.execute("""
    SELECT * FROM chat_history
    ORDER BY id DESC
    LIMIT 10
    """)
    chats = cursor.fetchall()

    conn.close()

    return (
        total_queries,
        property_count,
        consumer_count,
        cybercrime_count,
        government_count,
        chats
    )