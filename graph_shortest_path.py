from collections import deque

def build_graph(graph_str):
    graph = {}
    for line in graph_str.split('\n'):
        if line.strip():
            vertex, neighbors = map(str.strip, line.split('->'))
            graph[vertex] = neighbors.split(',')
    return graph

def bfs_shortest_path(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        vertex, path = queue.popleft()
        if vertex == end:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

def main():
    graph_str = """
    1->2
    2->3,4,6
    3->4,5,2
    4->2,3,5,6
    5->4,3,6
    6->2,4,5
    """

    graph = build_graph(graph_str)

    start = '1'
    end = '6'

    shortest_path = bfs_shortest_path(graph, start, end)

    if shortest_path:
        with open('log.txt', 'w', encoding='utf-8') as f:
            f.write(f"Кратчайший путь из вершины {start} в вершину {end}: {' -> '.join(shortest_path)}")
        print("Результат записан в log.txt")
    else:
        print("Пути между вершинами нет.")

if __name__ == "__main__":
    main()
