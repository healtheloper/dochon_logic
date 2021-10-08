const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
const input = [];

const solution = (input) => {
  const [data, ...rest] = input;
  const [a, b, c] = data.split(" ");
  const graph = new Array(+a + 1).fill(null).map((v) => []);
  rest.forEach((point) => {
    const [to, from] = point.split(" ");
    graph[to].push(+from);
    graph[from].push(+to);
  });

  graph.forEach((v) => {
    v.sort((a, b) => a - b);
  });

  const bfsVisited = new Array(+a + 1).fill(false);
  const dfsVisited = new Array(+a + 1).fill(false);
  const bfsArray = [];
  const dfsArray = [];
  const bfs = (start) => {
    bfsVisited[start] = true;
    queue = [start];
    while (queue.length > 0) {
      const q = queue.shift();
      bfsArray.push(q);
      graph[q].forEach((v) => {
        if (!bfsVisited[v]) {
          bfsVisited[v] = true;
          queue.push(v);
        }
      });
    }
  };
  const dfs = (start) => {
    dfsVisited[start] = true;
    dfsArray.push(start);
    graph[start].forEach((v) => {
      if (!dfsVisited[v]) {
        dfs(v);
      }
    });
  };
  bfs(+c);
  dfs(+c);
  return [dfsArray.join(" "), bfsArray.join(" ")].join("\n");
};

rl.on("line", (answer) => {
  input.push(answer.trim());
}).on("close", () => {
  console.log(solution(input));
});
