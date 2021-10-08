const graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7],
];
const visited = new Array(9).fill(false);

const bfs = (graph, start, visited) => {
  visited[start] = true;
  const queue = [start];

  while (queue.length > 0) {
    v = queue.shift();
    console.log(v);
    graph[v].forEach((i) => {
      if (!visited[i]) {
        queue.push(i);
        visited[i] = true;
      }
    });
  }
};

bfs(graph, 1, visited); // 1 2 3 8 7 4 5 6
