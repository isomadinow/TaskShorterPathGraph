import json

def extract_companies(data):
    # Инициализация списка для хранения найденных компаний
    companies = []

    # Внутренняя рекурсивная функция для обхода дерева
    def recursive_search(node):
        # Проверка, содержит ли узел необходимые ключи
        if 'title' in node and 'id' in node:
            # Добавление кортежа (title, id) в список
            companies.append((node['title'], node['id']))
        
        # Рекурсивный вызов для всех дочерних узлов
        if 'children' in node:
            for child in node['children']:
                recursive_search(child)
    
    # Запуск рекурсивного поиска с корневого узла
    recursive_search(data)
    
    return companies

# Пример использования
with open('new_test_hw.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

result = extract_companies(data)
print(result)
