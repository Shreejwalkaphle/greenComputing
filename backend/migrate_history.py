from database import get_connection

def create_history_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluation_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hardware TEXT,
            devices INTEGER,
            hours REAL,
            country TEXT,
            energy_kwh REAL,
            carbon_kg REAL,
            green_score REAL
        )
    """)

    conn.commit()
    conn.close()
    print("Evaluation history table created.")

if __name__ == "__main__":
    create_history_table()
