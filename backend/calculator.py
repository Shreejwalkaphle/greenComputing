from standards import HARDWARE_POWER, COUNTRY_CARBON, BASELINE_CARBON

def calculate_green_score(data):
    power = HARDWARE_POWER[data["hardware"]]
    carbon_intensity = COUNTRY_CARBON[data["country"]]

    energy = power * data["devices"] * data["hours"]
    carbon = energy * carbon_intensity

    score = max(0, 100 - (carbon / BASELINE_CARBON) * 100)

    return {
        "energy_kwh": round(energy, 2),
        "carbon_kg": round(carbon, 2),
        "green_score": round(score, 2)
    }


if __name__ == "__main__":
    sample_data = {
        "hardware": "A100",
        "devices": 2,
        "hours": 10,
        "country": "USA"
    }

    result = calculate_green_score(sample_data)
    print(result)
