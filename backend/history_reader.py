from database import get_connection

def get_all_history():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT hardware, devices, hours, country,
               energy_kwh, carbon_kg, green_score
        FROM evaluation_history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    history = []
    for row in rows:
        history.append({
            "hardware": row[0],
            "devices": row[1],
            "hours": row[2],
            "country": row[3],
            "energy_kwh": row[4],
            "carbon_kg": row[5],
            "green_score": row[6],
        })

    return history
