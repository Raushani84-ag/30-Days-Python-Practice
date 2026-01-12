def normalize_energy_record(record):
    """
    Normalize a validated energy record.

    """
    normalized = record.copy()

    normalized['site_id'] = normalized['site_id'].strip().upper()
    normalized['demand_kw'] = float(normalized['demand_kw'])

    return normalized

if  __name__ == "__main__":

    record = {
        "site_id": " s1 ",
        "timestamp": "2024-01-01 08:00",
        "demand_kw": 120
    }

    print(normalize_energy_record(record))


