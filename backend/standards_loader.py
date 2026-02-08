from database import get_connection

def get_hardware_power(hardware: str) -> float:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT power_kw FROM hardware_power WHERE hardware = ?",
        (hardware,)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        raise ValueError("Unknown hardware")


def get_country_carbon(country: str) -> float:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT carbon_intensity FROM country_carbon WHERE country = ?",
        (country,)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        raise ValueError("Unknown country")
