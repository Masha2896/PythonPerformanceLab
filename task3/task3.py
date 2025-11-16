import json
import sys


def fill_values(test_structure, values_map):
    if isinstance(test_structure, dict):
        if 'id' in test_structure:
            element_id = test_structure['id']
            if element_id in values_map:
                test_structure['value'] = values_map[element_id]

        for key in test_structure:
            fill_values(test_structure[key], values_map)

    elif isinstance(test_structure, list):
        for item in test_structure:
            fill_values(item, values_map)

def main():
    if len(sys.argv) != 4:
        print("Использование: python program.py <tests.json> <values.json> <report.json>")
        sys.exit(1)

    tests_path = sys.argv[1]
    values_path = sys.argv[2]
    report_path = sys.argv[3]

    try:
        with open(tests_path, 'r', encoding='utf-8') as f:
            tests_data = json.load(f)

        with open(values_path, 'r', encoding='utf-8') as f:
            values_data = json.load(f)

        values_map = {}
        for item in values_data['values']:
            values_map[item['id']] = item['value']

        fill_values(tests_data, values_map)

        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(tests_data, f, indent=2, ensure_ascii=False)

        print(f"Отчет успешно сохранен в {report_path}")

    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e}")
    except json.JSONDecodeError as e:
        print(f"Ошибка: Неверный формат JSON - {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()