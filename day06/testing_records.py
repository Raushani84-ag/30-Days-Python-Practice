from validation import validate_energy_record , validate_energy_batch
from normalization import normalize_energy_record

records = [
    {"site_id": " s1 ", "timestamp": "2024-01-01 08:00", "demand_kw": 120},
    {"site_id": None, "timestamp": "2024-01-01 09:00", "demand_kw": 80},
    {"site_id": "s2", "timestamp": "bad_time", "demand_kw": 50},
    {"site_id": " S3 ", "timestamp": "2024-01-01 10:00", "demand_kw": 200},
]

def validate_and_normalize_record(records):
    normalized_records = []

    valid_records, invalid_records = validate_energy_batch(records)

    for record in valid_records:
        normalized_record = normalize_energy_record(record)
        normalized_records.append(normalized_record)

    return normalized_records

normalized_energy_records =  validate_and_normalize_record(records)
print(normalized_energy_records)
print(len(normalized_energy_records))

