
from database import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Create hardware table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hardware_power (
            hardware TEXT PRIMARY KEY,
            power_kw REAL
        )
    """)

    # Create country carbon table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS country_carbon (
            country TEXT PRIMARY KEY,
            carbon_intensity REAL
        )
    """)

    # Insert dummy data
    cursor.executemany("""
        INSERT OR REPLACE INTO hardware_power (hardware, power_kw)
        VALUES (?, ?)
    """, [
        ("A100", 0.4),
        ("V100", 0.3),
        ("RTX3090", 0.35),
        ("CPU", 0.15)
    ])

    cursor.executemany("""
        INSERT OR REPLACE INTO country_carbon (country, carbon_intensity)
        VALUES (?, ?)
    """, [
        ("USA", 0.4),
        ("Germany", 0.35),
        ("India", 0.7),
        ("Norway", 0.02)
    ])

    conn.commit()
    conn.close()
    print("Database initialized with standard data.")

if __name__ == "__main__":
    init_db()
