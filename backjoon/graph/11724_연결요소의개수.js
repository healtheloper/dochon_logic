// 순환되는 그래프여야한다고 생각했음
// 단순히 '방문했는지' 를 확인하면 됐음 - 1012 유기농배추 문제와 유사

// N, M (M 이 0 일때, 즉 M 은 N-1 이 보장되지 않음)
// 연결 요소 라는 말때문에 간선이어야 된다고 생각했는데 단순한 점 하나도 카운트 되는 것
// 엣지케이스 잘 생각

const input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

const solution = (input) => {
  const [count, ...rest] = input;
  const [N, M] = count.split(' ').map((v) => +v);

  const graph = {};
  let paths = 0;

  rest.forEach((edges) => {
    const [u, v] = edges.split(' ').map((v) => +v);
    if (graph[u]) {
      graph[u].push(v);
    } else {
      graph[u] = [v];
    }
    if (graph[v]) {
      graph[v].push(u);
    } else {
      graph[v] = [u];
    }
  });

  const visited = new Array(N + 1).fill(false);

  const dfs = (start) => {
    visited[start] = true;
    const linkedPath = graph[start];
    if (!linkedPath) return;
    for (let i = 0; i < linkedPath.length; i++) {
      const point = graph[start][i];
      if (!visited[point]) {
        dfs(point);
      }
    }
  };

  new Array(N)
    .fill(0)
    .map((_, i) => i + 1)
    .forEach((point) => {
      if (!visited[point]) {
        paths += 1;
        dfs(point);
      }
    });

  return paths;
};

console.log(solution(input));
