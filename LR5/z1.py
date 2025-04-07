import re

def is_zip_code(zip_code):
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))

def validate_zip_code(zip_code):
    if not is_zip_code(zip_code):
        raise ValueError("Некорректный формат почтового индекса")
    return zip_code

try:
    zip_code = "1234"
    if is_zip_code(zip_code):
        print(f"'{zip_code}' является почтовым индексом.")
except ValueError as e:
    print(e)