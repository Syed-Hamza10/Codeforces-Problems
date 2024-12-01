import sys

def floyd_warshall(n, graph):
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dist[i][i] = 0
        
    for u in range(1, n + 1):
        for v, d in graph[u]:
            dist[u][v] = d
            dist[v][u] = d
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

def find_best_router(n, dist):
    min_avg_distance = float('inf')
    best_building = -1
    
    for i in range(1, n + 1):
        avg_distance = sum(dist[i][1:]) / (n - 1)
        
        if avg_distance < min_avg_distance:
            min_avg_distance = avg_distance
            best_building = i
        elif avg_distance == min_avg_distance:
            best_building = min(best_building, i)
    
    return best_building

def main():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n + 1)]
        
        for _ in range(m):
            u, v, d = input().split()
            u, v, d = int(u), int(v), float(d)
            graph[u].append((v, d))
            graph[v].append((u, d))
        
        dist = floyd_warshall(n, graph)
        result = find_best_router(n, dist)
        print(result)

if __name__ == '__main__':
    main()
