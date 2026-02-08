from database import get_connection

def save_evaluation(data, result):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO evaluation_history (
            hardware, devices, hours, country,
            energy_kwh, carbon_kg, green_score
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["hardware"],
        data["devices"],
        data["hours"],
        data["country"],
        result["energy_kwh"],
        result["carbon_kg"],
        result["green_score"]
    ))

    conn.commit()
    conn.close()
