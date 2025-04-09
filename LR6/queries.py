import sqlite3
import os


def run_queries():
    db_path = os.path.join(os.path.dirname(__file__), 'employment_agency.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    print("\n=== Статистика по кадровому агентству ===\n")

    # Запрос 1: Количество сотрудников по должностям
    cursor.execute('''
    SELECT p.title, COUNT(e.id) as count 
    FROM positions p
    LEFT JOIN employees e ON p.id = e.position_id
    GROUP BY p.title
    ''')
    print("1. Количество сотрудников по должностям:")
    for row in cursor.fetchall():
        print(f"  - {row[0]}: {row[1]} чел.")

    # Запрос 2: Средний возраст и стаж
    cursor.execute('''
    SELECT 
        AVG(age) as avg_age,
        AVG(experience) as avg_exp
    FROM employees
    ''')
    avg_age, avg_exp = cursor.fetchone()
    print(f"\n2. Средний возраст сотрудников: {avg_age:.1f} лет")
    print(f"   Средний стаж работы: {avg_exp:.1f} лет")

    # Запрос 3: Соотношение открытых/закрытых заявок
    cursor.execute('''
    SELECT 
        SUM(CASE WHEN status = 'open' THEN 1 ELSE 0 END) as open,
        SUM(CASE WHEN status = 'closed' THEN 1 ELSE 0 END) as closed
    FROM applications
    ''')
    open_apps, closed_apps = cursor.fetchone()
    print(f"\n3. Заявки: открытые — {open_apps}, закрытые — {closed_apps}")

    conn.close()


if __name__ == "__main__":
    run_queries()