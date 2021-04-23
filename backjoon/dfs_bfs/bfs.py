from collections import deque

# BFS 메서드 정의
# BFS -> 두 노드 사이의 최단 경로를 찾고 싶을 때 해당 방법 선택
# DFS는 경로의 특징을 저장해둬야 하는 문제, 검색대상 그래프가 많다면,
# BFS는 최단거리를 찾아야 할 때, 검색 시작 지점으로부터 대상이 별로 멀지 않다면,

## 검색 속도 BFS > DFS
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)