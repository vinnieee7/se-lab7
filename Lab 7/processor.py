def sanitize_meter_id(meter_id):
    """
    Sanitizes a meter ID by stripping whitespace, removing specified prefix
    characters (!, @, #, $, %), and converting to uppercase.
    Handles null or non-string inputs safely without crashing.
    """
    if meter_id is None or not isinstance(meter_id, str):
        return ""
    meter_id = meter_id.strip()
    for ch in ['!', '@', '#', '$', '%']:
        meter_id = meter_id.replace(ch, '')
    return meter_id.upper()


def parse_consumption_readings(readings_csv):
    """
    Parses a comma-separated string of consumption readings into a list of integers.
    Handles null, empty, non-string, or malformed entries safely without crashing.
    """
    if readings_csv is None or not isinstance(readings_csv, str):
        return []
    readings = readings_csv.split(',')
    parsed = []
    for r in readings:
        try:
            parsed.append(int(r.strip()))
        except (ValueError, TypeError, AttributeError):
            continue
    return parsed


def format_billing_summary(account_record):
    """
    Formats an account record given as 'CustomerName:UsageUnits:Zone'.
    Returns a formatted summary string.
    Handles null, empty, non-string, missing fields, or invalid integers safely without crashing.
    """
    if account_record is None or not isinstance(account_record, str):
        return "Invalid account record"
    parts = account_record.split(':')
    if len(parts) < 3:
        return "Invalid account record"
    customer_name = parts[0].strip()
    try:
        units = int(parts[1].strip())
    except (ValueError, TypeError, AttributeError):
        return "Invalid account record"
    zone = parts[2].strip()
    return f"Customer {customer_name} billed {units * 2} USD in {zone}"


def main():
    print("==== Running sanitize_meter_id ====")
    raw_id = input("Enter a meter ID with prefixes (!,@,#,$,%): ")
    clean_id = sanitize_meter_id(raw_id)
    print("Sanitized Meter ID:", clean_id)

    print("\n==== Running parse_consumption_readings ====")
    csv_input = input("Enter consumption readings (e.g. 10,25,30): ")
    readings_list = parse_consumption_readings(csv_input)
    print("Parsed Readings:", readings_list)

    print("\n==== Running format_billing_summary ====")
    summary_input = input("Enter account record (Name:Usage:Zone): ")
    summary = format_billing_summary(summary_input)
    print("Billing Summary:", summary)


if __name__ == "__main__":
    main()
