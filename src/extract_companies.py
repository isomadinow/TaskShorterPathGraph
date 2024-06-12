import json

def extract_companies(data):
    companies = []
    def recursive_search(node):
        if 'title' in node and 'id' in node:
            companies.append((node['title'], node['id']))
        if 'children' in node:
            for child in node['children']:
                recursive_search(child)
    recursive_search(data)
    return companies

with open('assets/file/new_test_hw.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    
result = extract_companies(data)
print(result)
