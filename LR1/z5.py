import re

def find_dates(input_str):
    pattern = re.compile(
        r'\b(?:0?[1-9]|[12]\d|3[01])\s+'
        r'(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s+'
        r'\d{4}\b',
        re.IGNORECASE
    )
    return pattern.findall(input_str)

def main():
    sample_text = (
        "Сегодня 10 апреля 2021, а вчера было 07 февраля 2020. "
        "Также в истории отмечается событие 31 февраля 2007, "
        "которое, возможно, является ошибочным. "
        "Некоторые записи: 29 февраля 2020, 1 января 1999, и 15.03.2018."
    )

    print("Исходная строка:")
    print(sample_text)
    print("\nНайденные даты:")

    dates = find_dates(sample_text)
    if dates:
        for date in dates:
            print(date)
    else:
        print("Даты в заданном формате не найдены.")


if __name__ == "__main__":
    main()
