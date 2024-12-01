import heapq
from collections import defaultdict

def find_route(test_cases):
    results = []

    for test in test_cases:
        n, m, connections = test["N"], test["M"], test["connections"]

        graph = defaultdict(list)
        for u, v, d in connections:
            graph[u].append((v, d))
            graph[v].append((u, d))

        def dijkstra(start):
            distances = {i: float('inf') for i in range(1, n + 1)}
            distances[start] = 0
            pq = [(0, start)]

            while pq:
                curr_dist, curr_node = heapq.heappop(pq)

                if curr_dist > distances[curr_node]:
                    continue

                for neighbor, weight in graph[curr_node]:
                    new_dist = curr_dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))

            return distances

        best_node = -1
        min_avg_delay = float('inf')

        for node in range(1, n + 1):
            distances = dijkstra(node)
            total_delay = 0
            reachable = 0

            for i in range(1, n + 1):
                if distances[i] < float('inf'):
                    total_delay += distances[i]
                    reachable += 1

            if reachable > 1:
                avg_delay = total_delay / (reachable - 1)
            else:
                continue

            if avg_delay < min_avg_delay or (avg_delay == min_avg_delay and node < best_node):
                min_avg_delay = avg_delay
                best_node = node

        results.append(best_node)

    return results

if __name__ == "__main__":
    T = int(input())
    test_cases = []

    for _ in range(T):
        n, m = map(int, input().split())
        connections = []

        for _ in range(m):
            u, v, d = map(int, input().split())
            connections.append((u, v, d))

        test_cases.append({"N": n, "M": m, "connections": connections})

    results = find_route(test_cases)
    for r in results:
        print(r)
