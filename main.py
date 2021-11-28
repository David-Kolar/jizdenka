from pqdict import minpq


def dijkstra(graph, source, target=None):
    """source: https://gist.github.com/nvictus/7854213"""
    dist = {}  # lengths of the shortest paths to each node
    pred = {}  # predecessor node in each shortest path

    # Store distance scores in a priority queue dictionary
    pq = minpq()
    for node in graph:
        if node == source:
            pq[node] = 0
        else:
            pq[node] = float('inf')

    # popitems always pops out the node with min score
    # Removing a node from pqdict is O(log n).
    for node, min_dist in pq.popitems():
        dist[node] = min_dist
        if node == target:
            break

        for neighbor in graph[node]:
            if neighbor in pq:
                new_score = dist[node] + graph[node][neighbor]
                if new_score < pq[neighbor]:
                    # Updating the score of a node is O(log n) using pqdict.
                    pq[neighbor] = new_score
                    pred[neighbor] = node

    return dist


def shortest_path(graph, source, target):
    dist, pred = dijkstra(graph, source, target)
    end = target
    path = [end]
    while end != source:
        end = pred[end]
        path.append(end)
    path.reverse()
    return path


def make_graph(n=5, paths=()):
    graph = dict()
    for i in range(1, n + 1):
        graph[str(i)] = {}
    for a, b, distance in paths:
        graph[a].update({b: distance})
        graph[b].update({a: distance})
    return graph


def file_input():
    with open("input") as file:
        first = True
        paths = []
        for line in file:
            if (first):
                number, path_n, price, group_price = [int(n) for n in line.split()]
                first = False
                continue
            node = line.split()
            node[2] = int(node[2])
            paths.append(node)
    return number, paths, price, group_price


def file_output(n):
    with open("output", "w") as file:
        file.write(str(n))


def find_min(a, b, c, n, price, group):
    min = float("inf")
    for city in range(1, n + 1):
        city = str(city)
        actual_cost = (a[city] + b[city]) * price + c[city] * group
        if (actual_cost < min):
            min = actual_cost
    return min


n, paths, price, group_price = file_input()
graph = make_graph(n, paths)
alice = dijkstra(graph, source="1")
bob = dijkstra(graph, source="2")
carol = dijkstra(graph, source="3")
min = find_min(alice, bob, carol, n, price, group_price)
file_output(min)
