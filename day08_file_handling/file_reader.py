def read_raw_file(file_path):
    """
    read raw energy data line by line.
    """
    lines = []
    with open(file_path , 'r', encoding= 'utf-8') as file:
        for line in file:
            lines.append(line)

    return lines

def parse_energy_lines(lines):
    """
        Parse raw file lines into structured records.
        Skips malformed lines safely.
    """
    records = []
    errors =[]

    for line_no , line in enumerate(lines, start= 1):
        parts = line.split(",")

        if len(parts) != 3:
            errors.append((line_no, line, "Malformed line"))
            continue

        site_id , timestamp, demand_kw = parts
        site_id = site_id.strip()
        timestamp = timestamp.strip()
        demand_kw = demand_kw.strip()

        if not site_id:
            errors.append((line_no,"Missing site_id"))
            continue

        try:
            demand_kw = float(demand_kw)

        except ValueError:
            errors.append((line_no,"Invalid demand value"))
            continue

        record = {
            'site_id ': site_id,
            'timestamp': timestamp,
            'demand_kw' : demand_kw
        }

        records.append(record)

    return records, errors

def write_clean_records(records, output_path):
    """
    write cleaned energy records to a file
    """
    with open(output_path, 'w') as file:
        for record in records:
            line = f"{record['site_id']}, {record['timestamp']}, {record['demand_kw']}"
            file.write(line)

def write_error_log(errors, log_path):
    """
    write parsing errors to a log file.
    """
    with open(log_path , 'w') as file:
        for line_no , line , reason in errors:
            log_line = f'line{line_no}| {line}|{reason}\n'
            file.write(log_line)


if  __name__ ==  "__main__":
    data_lines = read_raw_file(file_path = 'raw_energy_data.txt')

    records, errors = parse_energy_lines(data_lines)
    print("Parsed Records : \n" )
    for r in records:
        print(r)


    print("Parsed Errors : \n")
    for e in errors:
        print(e)

    write_clean_records(records, "cleaned_energy_data.txt")
    write_error_log(errors, "processing_log.txt")

