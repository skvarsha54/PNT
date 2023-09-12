graph = {
    'Kiev': ['Prague'],
    'Prague': ['Zurich'],
    'Zurich': ['Amsterdam'],
    'Amsterdam': ['Barcelona'],
    'Barcelona': ['Berlin'],
    'Berlin': ['Kiev', 'Amsterdam'],
    'Paris': ['Skopje'],
    'Skopje': ['Paris']
}


def find_route(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for city in graph[start]:
        if city not in path:
            new_path = find_route(graph, city, end, path)
            if new_path:
                return new_path
    return None

start_city = 'Kiev'
end_city = 'Barcelona'
route = find_route(graph, start_city, end_city)

if route:
    print(f"Your son's route from {start_city} to {end_city}:")
    print(' -> '.join(route))
else:
    print(f"No route found from {start_city} to {end_city}.")