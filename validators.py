def is_valid_amount(value):
    try:
        return float(value)>=0
    except ValueError:
        return False
