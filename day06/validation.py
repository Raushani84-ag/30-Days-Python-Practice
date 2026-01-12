from datetime import datetime


def is_valid_timestamp(timestamp_str):
    """
        Check if a timestamp string is valid.

        Expected format: YYYY-MM-DD HH:MM
        Returns True if valid, False otherwise.
        """
    if timestamp_str is None:
        return False
    try:
        datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
        return True

    except(ValueError, TypeError):
        return False



def validate_energy_record(record):
    """
        Validate a single energy record.

        Returns:
            (True, None) if valid
            (False, error_message) if invalid
        """
    if not isinstance(record, dict):
        return False, "Record must be a dictionary"

    site_id = record.get("site_id")
    if not site_id or not isinstance(site_id, str):
        return False, "Invalid or missing site_id"

    timestamp = record.get("timestamp")
    if not is_valid_timestamp(timestamp):  # Reusing Task 1 method
        return False, "Invalid timestamp format"

    demand = record.get("demand_kw", 0)
    if not isinstance(demand, (int, float)):
        return False, "demand_kw must be numeric"

    if demand < 0:
        return False, "demand_kw must be non-negetive"

    return True, None



def validate_energy_batch(records):
    """
        Validate a list of energy records.

        Returns:
            valid_records: list of valid records
            invalid_records: list of (record, error_message)
        """
    if not isinstance(records, list):
        raise TypeError("records must be a list")

    valid_records = []
    invalid_records = []

    for record in records:
        is_valid, error = validate_energy_record(record)

        if is_valid:
            valid_records.append(record)
        else:
            invalid_records.append((record, error))

    return valid_records, invalid_records

if __name__ == "__main__":

    records = [
        {"site_id": "S1", "timestamp": "2024-01-01 08:00", "demand_kw": 120},
        {"site_id": None, "timestamp": "2024-01-01 09:00", "demand_kw": 80},
        {"site_id": "S2", "timestamp": "bad_time", "demand_kw": 50},
    ]

    valid, invalid = validate_energy_batch(records)
    print(f'valid records:  {valid}')
    print(f'invalid records:  {invalid}')




