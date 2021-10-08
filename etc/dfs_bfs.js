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

const bfsArray = [];
const dfsArray = [];

const dfsVisited = new Array(9).fill(false);
const dfs = (graph, start) => {
  dfsVisited[start] = true;
  dfsArray.push(start);
  graph[start].forEach((i) => {
    if (!dfsVisited[i]) {
      dfs(graph, i);
    }
  });
};
const bfs = (graph, start) => {
  const visited = new Array(9).fill(false);
  visited[start] = true;
  const queue = [start];

  while (queue.length > 0) {
    v = queue.shift();
    bfsArray.push(v);
    graph[v].forEach((i) => {
      if (!visited[i]) {
        queue.push(i);
        visited[i] = true;
      }
    });
  }
};

bfs(graph, 1);
dfs(graph, 1);
console.log(bfsArray.join(" ")); // 1 2 3 8 7 4 5 6
console.log(dfsArray.join(" "));
