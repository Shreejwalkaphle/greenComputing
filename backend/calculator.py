from standards_loader import get_hardware_power, get_country_carbon

BASELINE_CARBON = 20


def generate_suggestions(data, carbon):
    suggestions = []

    if data["devices"] > 1:
        suggestions.append("Consider reducing the number of devices used for training.")

    if data["hours"] > 5:
        suggestions.append("Try optimizing training to reduce total training hours.")

    if data["country"] not in ["Norway", "Germany"]:
        suggestions.append("Using a region with greener energy sources can significantly reduce carbon emissions.")

    if carbon > 10:
        suggestions.append("Your carbon emission is high. Consider using more efficient hardware or pre-trained models.")

    return suggestions


def calculate_green_score(data):
    power = get_hardware_power(data["hardware"])
    carbon_intensity = get_country_carbon(data["country"])

    energy = power * data["devices"] * data["hours"]
    carbon = energy * carbon_intensity

    score = max(0, 100 - (carbon / BASELINE_CARBON) * 100)

    suggestions = generate_suggestions(data, carbon)

    return {
        "energy_kwh": round(energy, 2),
        "carbon_kg": round(carbon, 2),
        "green_score": round(score, 2),
        "suggestions": suggestions
    }
